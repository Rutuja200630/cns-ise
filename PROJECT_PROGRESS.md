# Project Progress & Phase Gate Tracking: `cns ise`

**Course:** Cryptography and Network Security (CNS) A.Y. 2026–27  
**Faculty In-Charge:** Prof. Renuka Pawar  
**Institution:** Sardar Patel Institute of Technology (SPIT), Mumbai  
**Project:** The Flexible Variable-Key Block Cipher Framework (Blowfish)  
**Research Investigation:** *Variable Key Length Impacts on Memory Allocation and Throughput in Blowfish Cryptographic Frameworks*  

---

## 1. Executive Summary & Status Dashboard

- **Current Operational Status:** **ALL 4 PHASES COMPLETED & VALIDATED; FINAL SUBMISSION PACKAGE READY**
- **Experimental Matrix Completion:** **1,820 / 1,820 Trials Completed (100.0%)**
- **Automated Unit Test Suite:** **14 / 14 Unit Tests Passed (100.0%)**
- **Validation Failures / Data Inconsistencies:** **0 (Zero)**
- **Total Research Figures Generated:** **12 Figures (300 DPI Publication Quality)**
- **Git Commit Hash:** `7b5963f` (`feat(cns-ise): implement strict phase-wise output management and 4-phase deliverables`)
- **Compiled Paper & Presentation:**
  - `ieee_research_paper.tex` (IEEEtran LaTeX source)
  - `paper.pdf` (1.83 MB publication manuscript)
  - `presentation.pptx` (1.39 MB 10-slide deck with speaker notes)

---

## 2. Phase-by-Phase Gate Audit

| Phase | Milestone Name | Mandatory Gate Check | Audit Result | Gate Status |
| :---: | :--- | :--- | :---: | :---: |
| **Phase 1** | **Data Lock & Pipeline Integrity** | Verify exact byte counts and SHA-256 digests for all 5 test workloads; freeze hardware & environment specifications. | 5/5 payloads verified; 64-bit block aligned; environment locked. | **PASSED & LOCKED** |
| **Phase 2** | **Local Tuning & Model Optimization** | Execute unit tests; tune warmups (3 reps) and timer (`perf_counter_ns`); separate pilot results from tournament data. | 14/14 tests passed; pilot raw/summary isolated in `pilot_results/`. | **PASSED & LOCKED** |
| **Phase 3** | **Tournament Benchmark Sync** | Execute full factorial matrix (14 keys × 5 workloads × 13 reps = 1,820 trials); verify 100% SHA-256 round-trip correctness; generate 12 figures. | 1,820 trials executed; 0 failures; 12 figures rendered at 300 DPI. | **PASSED & LOCKED** |
| **Phase 4** | **Overleaf Compilation & Cross-Review** | Assemble IEEEtran manuscript; verify authentic citations; compile 1.83 MB PDF; generate 10-slide PowerPoint presentation with speaker notes. | Full LaTeX paper compiled; authentic citations verified; Turnitin target <15%. | **PASSED & LOCKED** |
| **Final** | **Final Submission Package** | Verify canonical copies in `FINAL_SUBMISSION/` without erasing phase records; document source provenance. | All verified copies mapped to source phase; provenance logged. | **PASSED & READY** |

---

## 3. Detailed Deliverables & File Tracking

### Phase 1: Data Lock (`Phase_1_Data_Lock/`)
- `README.md` — Phase overview and data lock guide.
- `project_requirements.md` — Complete specification of institutional and cryptographic constraints.
- `experiment_config.json` — Immutable configuration defining 14 key sizes and 5 workloads.
- `environment_info.json` — Machine specifications (Intel64, Windows 10, 16 GB RAM, Python 3.9.13, PyCryptodome 4.2.0).
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
- `src/benchmark.py` — Benchmarking harness for pilot sweeps.
- `src/memory_profiler.py` — Dual-layer memory profiler (tracemalloc heap + psutil process RSS).
- `tests/` — Automated test suite:
  - `test_encryption.py` (6 passed)
  - `test_key_validation.py` (6 passed)
  - `test_benchmark_results.py` (2 passed)
- `pilot_results/pilot_raw.csv` & `pilot_summary.csv` — Isolated pilot benchmarking outputs.
- `analysis/parameter_comparison.csv` — Decision matrix evaluating warmups, operational modes, and execution models.
- `methodology/key_schedule_explanation.md` — Formal mathematical explanation of Blowfish Feistel rounds and 521 self-encryptions.
- `validation/phase_2_validation.txt` — Audit gate certification for Phase 2.
- `deliverables_manifest.csv` — Phase 2 manifest.

### Phase 3: Tournament Benchmark (`Phase_3_Tournament_Benchmark/`)
- `src/model_script.py` — Standardized execution script ready for evaluation and leaderboard logging.
- `src/statistics_analysis.py` — Descriptive stats, ANOVA, Kruskal-Wallis, linear regressions, 95% CIs.
- `src/visualization.py` — 300 DPI publication-quality figure generator.
- `src/validate_results.py` — Automated experimental validation and audit script.
- `raw_data/` — Raw experimental observations:
  - `benchmark_raw.csv` (1,820 individual trials | 669 KB)
  - `key_schedule_raw.csv` (420 initialization trials | 23.3 KB)
  - `memory_raw.csv` (Raw heap and RSS records | 174 KB)
- `processed_data/` — Aggregated summary statistics:
  - `benchmark_summary.csv` (140 configurations | 31.8 KB)
  - `key_schedule_results.csv` (Key schedule initialization statistics | 1.1 KB)
  - `memory_summary.csv` (Aggregated memory allocation summary | 10.2 KB)
- `graphs/` — 12 publication-quality 300 DPI figures (`fig01` to `fig12`).
- `tables/` — CSV and markdown formatted tables (`key_schedule_latency_table`, `throughput_comparison_table`, `memory_invariance_table`).
- `analysis/` — Hypothesis testing report (`statistical_analysis.md`) and empirical discussion (`results_and_discussion.md`).
- `environment/environment_report.json` — Frozen machine snapshot.
- `validation/validation_report.md` & `phase_3_validation.txt` — Audit sign-off for Phase 3.
- `deliverables_manifest.csv` — Phase 3 manifest.

### Phase 4: Overleaf Compilation (`Phase_4_Overleaf_Compilation/`)
- `paper/ieee_research_paper.tex` — Full two-column IEEEtran LaTeX source.
- `paper/references.bib` — Authentic BibTeX bibliography with full citations.
- `paper/paper.pdf` — Publication-ready compiled research paper manuscript (1.83 MB).
- `paper/compilation_log.txt` — Build log.
- `figures/` — Verified copies of all 12 publication figures from Phase 3.
- `tables/` — Verified copies of benchmark data tables.
- `results/results_and_discussion.md` — Written results discussion text.
- `presentation/presentation.pptx` — 10-slide PowerPoint presentation with styled corporate/academic layout and speaker notes (1.39 MB).
- `presentation/viva_preparation.md` — Slide-by-slide script and faculty viva Q&A.
- `review/cross_review_checklist.md` — Multi-author cross-review and Turnitin plagiarism checklist (<15% target).
- `validation/phase_4_validation.txt` — Audit gate sign-off for Phase 4.
- `deliverables_manifest.csv` — Phase 4 manifest.

### Final Submission (`FINAL_SUBMISSION/`)
- `model_script.py` — Standalone execution script.
- `final_benchmark_summary.csv` — Aggregated summary dataset.
- `graphs/` — Complete set of 12 research figures.
- `ieee_research_paper.tex` — IEEE LaTeX source.
- `references.bib` — Authentic bibliography.
- `final_report.pdf` — Compiled PDF paper (1.83 MB).
- `presentation.pptx` — Presentation deck (1.39 MB).
- `README.md` — Final submission guide.
- `faculty_submission_checklist.md` — Manifest audit checklist.
- `submission_status.md` — Provenance tracking record.

---

## 4. Next Action & Faculty Demonstration
All experimental, analytical, visualization, and documentation tasks are 100% complete. The project is ready for immediate presentation and viva defense before Prof. Renuka Pawar.
