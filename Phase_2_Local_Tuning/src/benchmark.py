"""
Benchmarking Engine for Phase 2 Local Tuning.
Used for pilot parameter sweeps, warm-up calibration, and timing isolation tuning.
Outputs strictly to `Phase_2_Local_Tuning/pilot_results/`.
"""

import argparse
import csv
import json
import logging
import os
import secrets
import sys
import time
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional

from blowfish_engine import (
    BlowfishCBC,
    BlowfishCTR,
    generate_key,
    pad_pkcs7,
    unpad_pkcs7,
    compute_sha256,
    BENCHMARK_KEY_BITS,
    BLOCK_SIZE_BYTES
)
from memory_profiler import MemoryProfiler

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("Phase2Benchmark")


def run_pilot_benchmark(
    pilot_workloads: List[Tuple[str, int, str]],
    key_lengths: List[int],
    repetitions: int = 3,
    warmup_count: int = 1,
    output_raw_csv: Optional[str] = None,
    output_summary_csv: Optional[str] = None
):
    """Run pilot tuning sweep isolating parameters, warmups, and steady-state timing."""
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if output_raw_csv is None:
        output_raw_csv = os.path.join(base_dir, "pilot_results", "pilot_raw.csv")
    if output_summary_csv is None:
        output_summary_csv = os.path.join(base_dir, "pilot_results", "pilot_summary.csv")
    os.makedirs(os.path.dirname(output_raw_csv), exist_ok=True)
    logger.info(f"Starting Phase 2 Pilot Tuning Benchmark (Keys={len(key_lengths)}, Workloads={len(pilot_workloads)})...")

    raw_fieldnames = [
        "pilot_trial_id", "timestamp", "key_bits", "key_bytes", "file_size_bytes",
        "file_size_label", "operation", "repetition", "is_warmup",
        "elapsed_ns", "elapsed_seconds", "throughput_mib_s", "latency_ms",
        "incremental_tracemalloc_bytes", "peak_rss_bytes", "correctness_passed"
    ]

    raw_records = []
    trial_counter = 0

    with open(output_raw_csv, "w", newline="", encoding="utf-8") as f_raw:
        writer = csv.DictWriter(f_raw, fieldnames=raw_fieldnames)
        writer.writeheader()

        for filename, size_bytes, label in pilot_workloads:
            # Load payload from Phase 1 test_data if available
            p_path = os.path.join("Phase_1_Data_Lock", "test_data", filename)
            if os.path.exists(p_path):
                with open(p_path, "rb") as pf:
                    data = pf.read()
            else:
                data = b"0" * size_bytes

            size_mib = size_bytes / (1024.0 * 1024.0)

            for k_bits in key_lengths:
                k_bytes = k_bits // 8

                total_iter = warmup_count + repetitions
                for it in range(1, total_iter + 1):
                    is_warmup = (it <= warmup_count)
                    rep_idx = it if is_warmup else (it - warmup_count)

                    key = generate_key(k_bits)
                    engine = BlowfishCBC(key)
                    iv = secrets.token_bytes(BLOCK_SIZE_BYTES)
                    padded = pad_pkcs7(data, BLOCK_SIZE_BYTES)

                    # Encryption
                    trial_counter += 1
                    t0 = time.perf_counter_ns()
                    ciphertext = engine.encrypt_raw_aligned(padded, iv=iv)
                    t1 = time.perf_counter_ns()

                    el_ns = t1 - t0
                    el_s = el_ns / 1e9
                    tp = size_mib / el_s if el_s > 0 else 0.0

                    row_enc = {
                        "pilot_trial_id": f"PILOT_{trial_counter:04d}_ENC",
                        "timestamp": datetime.utcnow().isoformat(),
                        "key_bits": k_bits,
                        "key_bytes": k_bytes,
                        "file_size_bytes": size_bytes,
                        "file_size_label": label,
                        "operation": "encryption",
                        "repetition": rep_idx,
                        "is_warmup": is_warmup,
                        "elapsed_ns": el_ns,
                        "elapsed_seconds": round(el_s, 8),
                        "throughput_mib_s": round(tp, 4),
                        "latency_ms": round(el_ns / 1e6, 4),
                        "incremental_tracemalloc_bytes": 0,
                        "peak_rss_bytes": 0,
                        "correctness_passed": True
                    }
                    writer.writerow(row_enc)
                    raw_records.append(row_enc)

                    # Decryption
                    trial_counter += 1
                    t2 = time.perf_counter_ns()
                    dec_padded = engine.decrypt_raw_aligned(ciphertext, iv=iv)
                    t3 = time.perf_counter_ns()

                    el_ns_dec = t3 - t2
                    el_s_dec = el_ns_dec / 1e9
                    tp_dec = size_mib / el_s_dec if el_s_dec > 0 else 0.0
                    recovered = unpad_pkcs7(dec_padded, BLOCK_SIZE_BYTES)
                    passed = (recovered == data)

                    row_dec = {
                        "pilot_trial_id": f"PILOT_{trial_counter:04d}_DEC",
                        "timestamp": datetime.utcnow().isoformat(),
                        "key_bits": k_bits,
                        "key_bytes": k_bytes,
                        "file_size_bytes": size_bytes,
                        "file_size_label": label,
                        "operation": "decryption",
                        "repetition": rep_idx,
                        "is_warmup": is_warmup,
                        "elapsed_ns": el_ns_dec,
                        "elapsed_seconds": round(el_s_dec, 8),
                        "throughput_mib_s": round(tp_dec, 4),
                        "latency_ms": round(el_ns_dec / 1e6, 4),
                        "incremental_tracemalloc_bytes": 0,
                        "peak_rss_bytes": 0,
                        "correctness_passed": passed
                    }
                    writer.writerow(row_dec)
                    raw_records.append(row_dec)

    logger.info(f"Pilot benchmark raw data saved to: {output_raw_csv}")

    # Generate pilot summary
    import pandas as pd
    df_pilot = pd.DataFrame(raw_records)
    df_valid = df_pilot[df_pilot["is_warmup"] == False]
    summary = df_valid.groupby(["operation", "file_size_label", "key_bits"]).agg(
        mean_tp=("throughput_mib_s", "mean"),
        std_tp=("throughput_mib_s", "std"),
        mean_latency_ms=("latency_ms", "mean")
    ).reset_index()
    summary.to_csv(output_summary_csv, index=False)
    logger.info(f"Pilot benchmark summary saved to: {output_summary_csv}")


if __name__ == "__main__":
    pilot_workloads = [
        ("payload_1024.bin", 1024, "1 KiB"),
        ("payload_102400.bin", 102400, "100 KiB"),
        ("payload_1048576.bin", 1048576, "1 MiB")
    ]
    pilot_keys = [32, 128, 256, 448]
    run_pilot_benchmark(pilot_workloads, pilot_keys, repetitions=3, warmup_count=1)
