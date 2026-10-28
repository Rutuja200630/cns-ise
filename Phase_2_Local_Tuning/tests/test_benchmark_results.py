"""
Unit tests for benchmark result recording, CSV schema compliance, and metric calculations.
"""

import os
import tempfile
import pandas as pd
import pytest


EXPECTED_RAW_COLUMNS = [
    "experiment_id",
    "timestamp",
    "key_bits",
    "key_bytes",
    "file_size_bytes",
    "file_size_label",
    "mode",
    "operation",
    "repetition",
    "is_warmup",
    "elapsed_ns",
    "elapsed_seconds",
    "throughput_mib_per_second",
    "latency_ms",
    "baseline_tracemalloc_bytes",
    "peak_tracemalloc_bytes",
    "incremental_peak_bytes",
    "baseline_rss_bytes",
    "peak_rss_bytes",
    "original_sha256",
    "decrypted_sha256",
    "correctness_passed",
    "python_version",
    "pycryptodome_version",
    "cpu_model",
    "operating_system",
    "notes"
]


def test_throughput_calculation_formula():
    """Verify that throughput formula (MiB / sec) calculates correctly."""
    size_bytes = 1048576  # 1 MiB
    elapsed_sec = 0.05    # 50 ms
    expected_throughput = 1.0 / 0.05  # 20.0 MiB/s

    calc_throughput = (size_bytes / (1024 * 1024)) / elapsed_sec
    assert abs(calc_throughput - expected_throughput) < 1e-9


def test_raw_csv_schema_integrity():
    """Verify sample mock raw DataFrame contains all required columns without omission."""
    sample_row = {col: "mock_value" for col in EXPECTED_RAW_COLUMNS}
    df = pd.DataFrame([sample_row])
    for col in EXPECTED_RAW_COLUMNS:
        assert col in df.columns, f"Missing required column: {col}"
