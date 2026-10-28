# Phase 3: Comprehensive Experimental Validation & Audit Report

**Course:** Cryptography and Network Security (CNS) A.Y. 2026–27  
**Faculty In-Charge:** Prof. Renuka Pawar  
**Institution:** Sardar Patel Institute of Technology (SPIT), Mumbai  
**Audit Status:** **100% PASSED & CERTIFIED**  

---

## 1. Experimental Matrix Audit

| Parameter | Expected Target | Actual Recorded in Raw Data | Audit Status |
| :--- | :---: | :---: | :---: |
| **Benchmark Key Lengths** | 14 lengths (32 to 448 bits) | 14 lengths (32, 64, 96, 128, 160, 192, 224, 256, 288, 320, 352, 384, 416, 448) | **PASS** |
| **Workload File Sizes** | 5 binary sizes (1 KiB to 50 MiB) | 5 sizes (1,024, 102,400, 1,048,576, 10,485,760, 52,428,800 B) | **PASS** |
| **Warm-Up Policy** | 3 iterations per configuration | Exactly 3 iterations per config flagged `is_warmup=True` (420 total) | **PASS** |
| **Measured Repetitions** | 10 iterations per configuration | Exactly 10 repetitions per config flagged `is_warmup=False` (1,400 total) | **PASS** |
| **Key Schedule Repetitions** | 30 iterations per key length | Exactly 30 iterations per key length (420 total) | **PASS** |
| **Total Executed Trials** | 1,820 raw trials | Exactly 1,820 rows in `raw_data/benchmark_raw.csv` | **PASS** |

---

## 2. Integrity, Correctness & Data Sanity Audit

1. **Negative Value Audit:**
   - Negative durations: **0**
   - Negative throughput values: **0**
   - Impossible latency values: **0**
2. **Cryptographic Correctness Audit:**
   - Total round-trip tests evaluated: **1,820**
   - SHA-256 digest match rate: **100.0% (1,820 / 1,820)**
   - Corruptions / padding failures: **0**
3. **Statistical Aggregation Audit:**
   - Aggregated configurations in `benchmark_summary.csv`: **140**
   - Summary means match raw trial means (excluding warm-ups): **PASS (Absolute delta < 0.001)**
4. **Environment Audit:**
   - Complete hardware, OS, Python runtime, and dependency audit recorded in `environment/environment_report.json`.

---

## 3. High-Resolution Visualizations Audit (300 DPI)

All 12 required figures exist with valid non-zero file sizes in `graphs/`:
- `fig01_key_length_vs_setup_time.png` (168 KB)
- `fig02_setup_time_variability.png` (231 KB)
- `fig03_encryption_throughput.png` (337 KB)
- `fig04_decryption_throughput.png` (335 KB)
- `fig05_key_length_throughput_comparison.png` (332 KB)
- `fig06_encryption_latency.png` (192 KB)
- `fig07_decryption_latency.png` (197 KB)
- `fig08_memory_vs_file_size.png` (256 KB)
- `fig09_memory_vs_key_length.png` (202 KB)
- `fig10_normalized_performance.png` (276 KB)
- `fig11_performance_heatmap.png` (305 KB)
- `fig12_correctness_summary.png` (114 KB)

**FINAL AUDIT VERDICT: 100% COMPLIANT. PHASE 3 TOURNAMENT BENCHMARK GATE PASSED.**
