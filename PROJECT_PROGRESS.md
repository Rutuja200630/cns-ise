# Project Progress & Phase Gate Tracking: `cns ise`

**Course:** Cryptography and Network Security (CNS) A.Y. 2026–27  
**Faculty In-Charge:** Prof. Renuka Pawar  
**Institution:** Sardar Patel Institute of Technology (SPIT), Mumbai  
**Project:** The Flexible Variable-Key Block Cipher Framework (Blowfish)  
**Research Investigation:** *Variable Key Length Impacts on Memory Allocation and Throughput in Blowfish Cryptographic Frameworks*  
**Student Lead:** Rutuja Hirudkar  

---

## 1. Executive Summary & Audited Status Dashboard

- **Current Operational Status:** **ALL 4 PHASES COMPLETED, SCIENTIFICALLY AUDITED, RECONCILED, AND VALIDATED**
- **Experimental Matrix Completion:** **1,820 / 1,820 Steady-State Trials (100.0%) + 490 Audited Key-Schedule Trials**
- **Automated Unit Test Suite:** **14 / 14 Unit Tests Passed (100.0% in 1.30s)**
- **Automated Results Validation Pipeline:** **PASSED (100% Compliant, 0 Errors)**
- **Cryptographic Correctness:** **100% Round-Trip SHA-256 Digest Match (0 Silent Failures)**
- **Total Research Figures Generated:** **12 Figures (300 DPI Publication Quality)**
- **Key-Schedule Latency Audit:** **Resolved Cold-Start Artifact** via 5-iteration warm-up policy; steady-state 32-bit mean dropped from 0.362 ms to 0.0896 ms (CV: 33.7%), aligning with all 14 key sizes (0.056–0.162 ms).
- **Three-Tier Memory Model Established:**
  - **Tier 1 (Theoretical Subkeys):** Exactly 4,168 bytes (18 P-array words + 1,024 S-box words), mathematically invariant to key length.
  - **Tier 2 (Python Heap `tracemalloc`):** Scales strictly with workload payload (~168.52 MiB for 50 MiB); variance across 32 to 448 bits $\le 186$ bytes ($<0.0001\%$).
  - **Tier 3 (Process RSS `psutil`):** Whole-process physical RAM working set stable at $\approx 265.6$ MiB.
- **Five-Workload Table Reconciled:** Table II in paper and Phase 3 tables compiled with all 5 workload columns (1 KiB, 100 KiB, 1 MiB, 10 MiB, 50 MiB) across 14 key sizes.
- **Compiled Paper & Presentation:**
  - `paper/ieee_research_paper.tex` (IEEEtran LaTeX source with 100% bijective citation match to `references.bib`)
  - `paper/paper.pdf` (Compiled publication manuscript with embedded figures and reconciled tables)
  - `presentation/presentation.pptx` (8-slide 16:9 widescreen deck with figures and audit findings)

---

## 2. Phase-by-Phase Gate Audit

| Phase | Milestone Name | Mandatory Gate Check | Audit Result | Gate Status |
| :---: | :--- | :--- | :---: | :---: |
| **Phase 1** | **Data Lock & Pipeline Integrity** | Verify exact byte counts and SHA-256 digests for all 5 test workloads; freeze hardware & environment specifications. | 5/5 payloads verified; 64-bit block aligned; environment locked. | **AUDITED & LOCKED** |
| **Phase 2** | **Local Tuning & Model Optimization** | Execute unit tests; tune warmups (3 reps) and timer (`perf_counter_ns`); separate pilot results from tournament data. | 14/14 tests passed; pilot raw/summary isolated in `pilot_results/`. | **AUDITED & LOCKED** |
| **Phase 3** | **Tournament Benchmark Sync** | Execute full factorial matrix (14 keys &times; 5 workloads &times; 13 reps = 1,820 trials); audit key schedule with warmups; verify 100% SHA-256 correctness; generate 12 figures. | 1,820 trials executed; 490 key schedule trials; 0 failures; 12 figures rendered at 300 DPI; `tournament_benchmark.py` verified. | **AUDITED & LOCKED** |
| **Phase 4** | **Overleaf Compilation & Cross-Review** | Assemble IEEEtran manuscript; verify authentic citations; compile PDF; generate PowerPoint presentation with speaker notes; reconcile all 5 workloads. | Full LaTeX paper compiled; authentic citations verified; 5-workload Table II reconciled; ReportLab PDF compiled. | **AUDITED & LOCKED** |
| **Final** | **Final Submission Package** | Verify canonical copies in `FINAL_SUBMISSION/` without erasing phase records; document source provenance. | All verified copies mapped to source phase; provenance logged in `submission_status.md`. | **AUDITED & READY** |

---

## 3. Audited Deliverables & Canonical File Locations

### Phase 1: Data Lock (`Phase_1_Data_Lock/`)
- `README.md` — Phase overview and data lock guide.
- `project_requirements.md` — Complete specification of institutional and cryptographic constraints.
- `experiment_config.json` — Immutable configuration defining 14 key sizes and 5 workloads.
- `environment_info.json` — Machine specifications (Intel64, Windows 10/11, 16 GB RAM, Python 3.9.13, PyCryptodome 4.2.0).
- `test_file_manifest.csv` — Table of verified test payloads, byte lengths, and SHA-256 digests.
- `test_data/` — 5 deterministic test payload binary files:
  - `payload_1024.bin` (1,024 B | SHA-256: `b98a2c4f...`)
  - `payload_102400.bin` (102,400 B | SHA-256: `87dc57b7...`)
  - `payload_1048576.bin` (1,048,576 B | SHA-256: `1aba1edd...`)
  - `payload_10485760.bin` (10,485,760 B | SHA-256: `731dfa62...`)
  - `payload_52428800.bin` (52,428,800 B | SHA-256: `2a139b32...`)
- `validation/phase_1_validation.txt` — Audit sign-off for Phase 1.
- `deliverables_manifest.csv` — Phase 1 manifest.

### Phase 2: Local Tuning (`Phase_2_Local_Tuning/`)
- `src/blowfish_engine.py` — Blowfish CBC/CTR engine with fresh IVs and PKCS#7 padding.
- `src/benchmark.py` — Benchmarking harness for pilot parameter sweeps.
- `src/memory_profiler.py` — Dual-layer memory profiler (tracemalloc heap + psutil process RSS).
- `tests/` — Automated test suite (14/14 passed in 1.30s):
  - `test_encryption.py` (6 passed)
  - `test_key_validation.py` (6 passed)
  - `test_benchmark_results.py` (2 passed)
- `pilot_results/pilot_raw.csv` & `pilot_summary.csv` — Isolated pilot benchmarking outputs (48 trials).
- `analysis/parameter_comparison.csv` — Decision matrix evaluating warmups, operational modes, and execution models.
- `methodology/key_schedule_explanation.md` — Formal mathematical explanation of Blowfish Feistel rounds and 521 self-encryptions.
- `validation/phase_2_validation.txt` — Audit gate certification for Phase 2.
- `deliverables_manifest.csv` — Phase 2 manifest.

### Phase 3: Tournament Benchmark (`Phase_3_Tournament_Benchmark/`)
- `src/tournament_benchmark.py` — Reproducible benchmarking executable supporting full matrix, warm-up policy, and table generation.
- `src/model_script.py` — Standardized execution script for faculty leaderboard evaluation.
- `src/statistics_analysis.py` — Descriptive stats, ANOVA, Kruskal-Wallis, linear regressions, 95% CIs.
- `src/visualization.py` — 300 DPI publication-quality figure generator for 12 research charts.
- `src/validate_results.py` — Automated experimental validation and audit script (100% pass).
- `raw_data/` — Raw experimental observations:
  - `benchmark_raw.csv` (1,820 individual trials | 669 KB)
  - `key_schedule_raw.csv` (490 initialization trials with warmups flagged | 27.5 KB)
  - `memory_raw.csv` (Raw heap and RSS records | 174 KB)
- `processed_data/` — Aggregated summary statistics:
  - `benchmark_summary.csv` (140 configurations | 31.8 KB)
  - `key_schedule_results.csv` (Key schedule initialization statistics excluding warm-ups | 1.1 KB)
  - `memory_summary.csv` (Aggregated memory summary with 3-tier data | 10.2 KB)
  - `statistical_test_results.json` (Formal ANOVA and Kruskal-Wallis JSON records)
- `graphs/` — 12 publication-quality 300 DPI figures (`fig01_key_vs_init_time.png` to `fig12_correctness_summary.png`).
- `tables/` — Reconciled CSV and markdown tables:
  - `throughput_comparison_table.csv` & `.md` (All 5 workloads across 14 key sizes)
  - `key_schedule_latency_table.csv` & `.md` (Audited steady-state values)
  - `memory_invariance_table.csv` & `.md` (Three-tier model at 50 MiB)
- `analysis/` — Hypothesis testing report (`statistical_analysis.md`) and empirical discussion (`results_and_discussion.md`).
- `environment/environment_report.json` — Frozen machine snapshot.
- `validation/validation_report.md` & `phase_3_validation.txt` — Audit sign-off for Phase 3.
- `deliverables_manifest.csv` — Phase 3 manifest.

### Phase 4: Overleaf Compilation (`Phase_4_Overleaf_Compilation/`)
- `paper/ieee_research_paper.tex` — Full two-column IEEEtran LaTeX source with reconciled tables, 3-tier memory model, and figures.
- `paper/references.bib` — Authentic BibTeX bibliography (7 peer-reviewed and official standards entries).
- `paper/compile_paper_pdf.py` — Local PDF compilation engine utilizing ReportLab.
- `paper/paper.pdf` — Publication-ready compiled research paper manuscript (1.05 MB).
- `figures/` — Verified copies of all 12 publication figures from Phase 3.
- `tables/` — Verified copies of benchmark data tables.
- `presentation/generate_presentation.py` — Automated presentation generator using `python-pptx`.
- `presentation/presentation.pptx` — 8-slide PowerPoint presentation with widescreen layout (0.82 MB).
- `review/viva_preparation.md` — Comprehensive faculty viva Q&A guide (7 core defense topics).
- `review/cross_review_checklist.md` — Multi-author cross-review and Turnitin plagiarism checklist (<15% target).
- `validation/phase_4_validation.txt` — Audit gate sign-off for Phase 4.
- `deliverables_manifest.csv` — Phase 4 manifest.

### Final Submission (`FINAL_SUBMISSION/`)
- `model_script.py` — Standalone execution script.
- `final_benchmark_summary.csv` — Aggregated summary dataset.
- `graphs/` — Complete set of 12 300 DPI research figures.
- `ieee_research_paper.tex` — Reconciled IEEE LaTeX source.
- `references.bib` — Authentic bibliography.
- `final_report.pdf` — Compiled PDF paper (1.05 MB).
- `presentation.pptx` — Presentation deck (0.82 MB).
- `README.md` — Final submission guide.
- `faculty_submission_checklist.md` — Manifest audit checklist.
- `submission_status.md` — Provenance tracking record.

---

## 4. Remaining Practical & Architectural Limitations

1. **Sweet32 Collision Boundary:** Blowfish operates on a 64-bit block size ($b = 64$). Under the Birthday Paradox, ciphertext block collisions occur with probability $p \ge 0.5$ after encrypting $2^{32}$ blocks ($\approx 32$ GiB of data). The Sweet32 attack (Bhargavan & Leurent, 2016) demonstrated that active network attackers can exploit ciphertext collisions in long-lived TLS or OpenVPN sessions to recover plaintext HTTP cookies. Consequently, Blowfish must not be deployed in modern high-throughput protocols regardless of key size.
2. **Software Cache-Timing Vulnerabilities:** Blowfish's non-linear round function relies on data-dependent lookups into four 256-word S-boxes. In shared virtualized cloud environments or multi-tenant CPU caches, cache-line access patterns can leak key material via cache-timing side channels (Flush+Reload, Prime+Probe).
3. **Interpreter Dispatch Overhead on Sub-Kilobyte Workloads:** For very small payloads (1 KiB), throughput is bounded at ~6.3–15.9 MiB/s due to Python-to-C dispatch overhead, object wrapping, and timer resolution, which does not reflect raw C algorithmic speed. Steady-state saturation is only attained for payloads $\ge 100$ KiB.

---

## 5. Local & Remote Verified Locations

- **Local Laptop Directory:** `c:\Users\Rutuja Hirudkar\OneDrive\c\amazon\cns ise\`
- **Remote Git Repository:** `https://github.com/Rutuja200630/cns-ise` (Branch: `main`)
- **Faculty Demonstration:** All experimental scripts, datasets, graphs, and presentation materials are ready for viva defense before Prof. Renuka Pawar.
