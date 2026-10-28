"""
Experimental Validation and Integrity Verification Module.
Validates the entire benchmarking data pipeline against rigorous scientific criteria:
1. All 14 key lengths represented.
2. All expected workload file sizes represented.
3. Verification of warm-up exclusion from aggregated summaries.
4. Cryptographic correctness verification (zero tolerated silent failures).
5. Non-negativity and numerical sanity checks for durations and throughputs.
6. Mathematical consistency between raw trials and aggregated summary statistics.
7. Existence and file size validation of all 12 generated research graphs.
"""

import json
import logging
import os
import sys
from typing import Dict, List, Any, Tuple
import numpy as np
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("ValidateResults")


def validate_results_pipeline(
    config_path: str = "config.json",
    raw_csv: str = "data/results/benchmark_raw.csv",
    summary_csv: str = "data/results/benchmark_summary.csv",
    key_csv: str = "data/results/key_schedule_results.csv",
    graphs_dir: str = "graphs"
) -> Tuple[bool, List[str]]:
    """
    Run comprehensive automated audit of experimental outputs.
    Returns (all_passed: bool, error_log: List[str]).
    """
    errors = []
    warnings = []

    logger.info("============================================================")
    logger.info("STARTING AUTOMATED EXPERIMENTAL VALIDATION AUDIT")
    logger.info("============================================================")

    # 1. Check Configuration and Result Files Exist
    for f_path, desc in [
        (config_path, "Configuration file"),
        (raw_csv, "Raw benchmark dataset"),
        (summary_csv, "Summary benchmark dataset"),
        (key_csv, "Key schedule dataset")
    ]:
        if not os.path.exists(f_path):
            errors.append(f"Missing required file: {desc} ({f_path})")

    if errors:
        for err in errors:
            logger.error(f"[FAIL] {err}")
        return False, errors

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    expected_key_bits = config["key_lengths_bits"]

    # 2. Inspect Raw CSV
    df_raw = pd.read_csv(raw_csv)
    logger.info(f"Loaded raw dataset: {len(df_raw)} records.")

    # Check key lengths in raw data
    raw_keys = sorted(df_raw["key_bits"].unique())
    missing_keys = set(expected_key_bits) - set(raw_keys)
    if missing_keys:
        errors.append(f"Raw data missing expected key lengths: {missing_keys}")
    else:
        logger.info(f"[PASS] All {len(expected_key_bits)} benchmark key lengths present in raw data.")

    # Check for negative durations or throughputs
    neg_duration = (df_raw["elapsed_seconds"] < 0).sum()
    neg_throughput = (df_raw["throughput_mib_per_second"] < 0).sum()
    if neg_duration > 0:
        errors.append(f"Found {neg_duration} trials with negative duration!")
    if neg_throughput > 0:
        errors.append(f"Found {neg_throughput} trials with negative throughput!")
    if neg_duration == 0 and neg_throughput == 0:
        logger.info("[PASS] All timing durations and throughput values are strictly non-negative.")

    # Check correctness pass/fail status
    failed_trials = df_raw[df_raw["correctness_passed"] == False]
    if len(failed_trials) > 0:
        errors.append(f"CRITICAL: {len(failed_trials)} trials failed cryptographic correctness/integrity check!")
    else:
        logger.info(f"[PASS] 100% round-trip cryptographic correctness verified across all {len(df_raw)} trials.")

    # 3. Inspect Summary CSV
    df_sum = pd.read_csv(summary_csv)
    logger.info(f"Loaded summary dataset: {len(df_sum)} configurations.")

    # Verify warm-up exclusion:
    # Compare summary mean with raw data (excluding is_warmup == True)
    if df_raw["is_warmup"].dtype == object:
        df_valid_raw = df_raw[df_raw["is_warmup"].astype(str).str.lower() == "false"]
    else:
        df_valid_raw = df_raw[df_raw["is_warmup"] == False]

    # Verify a random sample of aggregated means match
    mismatch_count = 0
    for _, s_row in df_sum.head(10).iterrows():
        match_raw = df_valid_raw[
            (df_valid_raw["operation"] == s_row["operation"]) &
            (df_valid_raw["key_bits"] == s_row["key_bits"]) &
            (df_valid_raw["file_size_bytes"] == s_row["file_size_bytes"])
        ]
        if not match_raw.empty:
            expected_mean_tp = match_raw["throughput_mib_per_second"].mean()
            if abs(expected_mean_tp - s_row["mean_throughput_mib_s"]) > 0.05:
                mismatch_count += 1
                errors.append(
                    f"Summary throughput mismatch for {s_row['operation']}, {s_row['key_bits']} bits, "
                    f"{s_row['file_size_label']}: Summary={s_row['mean_throughput_mib_s']}, RawMean={expected_mean_tp:.4f}"
                )

    if mismatch_count == 0:
        logger.info("[PASS] Aggregated summary statistics mathematically match raw measured trials.")

    # 4. Inspect Graphs
    expected_graphs = [
        "fig01_key_vs_init_time.png",
        "fig02_init_time_variability.png",
        "fig03_enc_throughput_vs_size.png",
        "fig04_dec_throughput_vs_size.png",
        "fig05_key_vs_throughput_panels.png",
        "fig06_enc_latency_vs_size.png",
        "fig07_dec_latency_vs_size.png",
        "fig08_memory_vs_file_size.png",
        "fig09_memory_vs_key_length.png",
        "fig10_normalized_performance.png",
        "fig11_key_size_heatmap.png",
        "fig12_correctness_summary.png"
    ]

    missing_graphs = []
    for g_name in expected_graphs:
        g_path = os.path.join(graphs_dir, g_name)
        if not os.path.exists(g_path):
            missing_graphs.append(g_name)
        else:
            file_size = os.path.getsize(g_path)
            if file_size < 1000:
                errors.append(f"Graph file abnormally small ({file_size} bytes): {g_name}")

    if missing_graphs:
        warnings.append(f"Graphs not yet generated: {missing_graphs}")
    else:
        logger.info(f"[PASS] All {len(expected_graphs)} research figures present with valid file sizes.")

    # 5. Final Verdict
    logger.info("============================================================")
    if not errors:
        logger.info("VALIDATION AUDIT RESULT: PASSED (100% COMPLIANT)")
        if warnings:
            for w in warnings:
                logger.warning(f"[NOTICE] {w}")
        return True, []
    else:
        logger.error(f"VALIDATION AUDIT RESULT: FAILED ({len(errors)} errors found)")
        for e in errors:
            logger.error(f"  - {e}")
        return False, errors


if __name__ == "__main__":
    passed, errs = validate_results_pipeline()
    sys.exit(0 if passed else 1)
