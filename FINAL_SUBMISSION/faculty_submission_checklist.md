# Faculty Submission Checklist & Collaborative R&D Deliverables

**Institution:** Sardar Patel Institute of Technology, Mumbai  
**Department:** Computer Engineering / Information Technology  
**Subject:** Cryptography and Network Security (CNS) A.Y. 2026–27  
**Faculty In-Charge:** Prof. Renuka Pawar  
**Project Title:** The Flexible Variable-Key Block Cipher Framework (Blowfish)  
**Research Topic:** *Variable Key Length Impacts on Memory Allocation and Throughput in Blowfish Cryptographic Frameworks*  

---

## 1. Master Tournament & Collaborative Timeline Mapping

This checklist maps our research project deliverables to the 4-week timeline specified in *Collaborative R&D Manifest: Comparative Algorithmic Analysis for Advanced Cybersecurity Domains* (Prof. Renuka Pawar).

| Milestone | Manifest Objective | Blowfish Research Implementation & Deliverable | Status |
| :--- | :--- | :--- | :---: |
| **Week 1: Data Lock & Pipeline Integrity** | Unified dataset generation, standardized data splits, preprocessing integrity. | Deterministic payload generation (1 KiB to 50 MiB) with cryptographic SHA-256 baseline hashing (`data/generated/`). Strict PKCS#7 block alignment and verification. | **Completed** |
| **Week 2: Isolated Model Optimization** | Hyperparameter sweeps, algorithmic tuning, model mathematical documentation. | Parameter sweeps across all 14 variable key lengths (32 to 448 bits). Mathematical isolation of key schedule expansion from steady-state block processing (`blowfish_engine.py`, `memory_profiler.py`). | **Completed** |
| **Week 3: Tournament Benchmark Sync** | Run standardized evaluation engine, profile sample latency, populate tournament matrix. | Execution of full factorial matrix (14 keys × 5 file sizes × 13 reps = 1,820 trials) on a single designated machine. Export to `benchmark_raw.csv` and `benchmark_summary.csv`. | **Completed** |
| **Week 4: Overleaf Compilation & Cross-Review** | Multi-author manuscript, mathematical equations, cross-model sync, bibliography, Turnitin. | Full IEEEtran two-column LaTeX paper (`ieee_research_paper.tex`), authentic BibTeX citations (`references.bib`), compiled PDF (`ieee_research_paper.pdf`), slide deck (`Blowfish_Benchmark_Presentation.pptx`), and viva defense script. | **Completed** |

---

## 2. Institutional Deliverables Checklist

### Core Software & Engineering Artifacts
- [x] **Main Execution Orchestrator:** `main.py` (Unified CLI supporting smoke, full, stats, visualize, validate, and all modes).
- [x] **Cryptographic Engine:** `blowfish_engine.py` (Blowfish CBC with fresh 64-bit IV per trial, PKCS#7 padding, variable key validation 32–448 bits, CTR mode, SHA-256 integrity check).
- [x] **Experimental Benchmark Engine:** `benchmark.py` (Isolated key-schedule timing, steady-state throughput/latency, incremental CSV logging).
- [x] **Dual-Layer Memory Profiler:** `memory_profiler.py` (Tracemalloc Python heap peak + psutil process RSS).
- [x] **System Environment Logger:** `system_info.py` (Records CPU, OS, RAM, Python version, PyCryptodome version to `system_environment.json`).
- [x] **Automated Validator:** `validate_results.py` (Rigorous schema check, zero failed trials check, non-negativity check, math consistency check).
- [x] **Configuration File:** `config.json` (Structured parameters for key sizes, file sizes, repetitions, paths).
- [x] **Pinned Dependencies:** `requirements.txt` (Pinned versions for PyCryptodome, NumPy, Pandas, Matplotlib, SciPy, Psutil, Pytest, Python-pptx, ReportLab).

### Automated Testing Suite
- [x] **Key Validation Tests:** `tests/test_key_validation.py` (Boundary checks, invalid length rejection, non-multiple-of-8 rejection).
- [x] **Encryption & Padding Tests:** `tests/test_encryption.py` (PKCS#7 round-trip, corruption rejection, boundary sizes 0 to 64 KiB, IV freshness, CTR mode).
- [x] **Benchmark Pipeline Tests:** `tests/test_benchmark_results.py` (Schema integrity, throughput formula correctness).
- [x] **Pytest Execution:** 14/14 automated unit tests passing.

### Experimental Datasets & Records
- [x] **Raw Trial Observations:** `data/results/benchmark_raw.csv` (Individual trials with timestamp, key bits/bytes, file size, operation, elapsed ns, throughput MiB/s, latency ms, memory, SHA-256 digests, pass/fail status).
- [x] **Aggregated Summary Dataset:** `data/results/benchmark_summary.csv` (Mean, median, std dev, min, max, 95% confidence intervals, excluding warm-up runs).
- [x] **Key Schedule Dataset:** `data/results/key_schedule_results.csv` and `key_schedule_summary.csv` (Initialization timing across 14 key sizes).
- [x] **Statistical Hypothesis Tests:** `data/results/statistical_test_results.json` (ANOVA, Kruskal-Wallis, linear regression on key schedule, throughput variance).
- [x] **System Environment JSON:** `data/results/system_environment.json` (Hardware, OS, and library audit trail).

### Publication-Quality Visualizations (300 DPI)
- [x] **Figure 1:** `graphs/fig01_key_vs_init_time.png` — Key Length vs. Cipher Initialization Time (ms, 95% CI).
- [x] **Figure 2:** `graphs/fig02_init_time_variability.png` — Key Length vs. Initialization Variability (Std Dev & CV %).
- [x] **Figure 3:** `graphs/fig03_enc_throughput_vs_size.png` — Encryption Throughput vs. File Size (MiB/s).
- [x] **Figure 4:** `graphs/fig04_dec_throughput_vs_size.png` — Decryption Throughput vs. File Size (MiB/s).
- [x] **Figure 5:** `graphs/fig05_key_vs_throughput_panels.png` — Key Length vs. Throughput at Each File Size (Multi-panel).
- [x] **Figure 6:** `graphs/fig06_enc_latency_vs_size.png` — Encryption Latency vs. File Size (ms).
- [x] **Figure 7:** `graphs/fig07_dec_latency_vs_size.png` — Decryption Latency vs. File Size (ms).
- [x] **Figure 8:** `graphs/fig08_memory_vs_file_size.png` — Memory Usage vs. File Size (Tracemalloc Heap vs. Process RSS).
- [x] **Figure 9:** `graphs/fig09_memory_vs_key_length.png` — Memory Usage vs. Key Length (Memory Invariance).
- [x] **Figure 10:** `graphs/fig10_normalized_performance.png` — Normalized Performance Comparison (Relative to 128-bit Key).
- [x] **Figure 11:** `graphs/fig11_key_size_heatmap.png` — Key Length × File Size Steady-State Throughput Heatmap.
- [x] **Figure 12:** `graphs/fig12_correctness_summary.png` — Cryptographic Correctness & Round-Trip Validation.

### Reports, Paper & Faculty Viva Deliverables
- [x] **Experimental Methodology Report:** `reports/experimental_methodology.md`.
- [x] **Results & Scientific Discussion:** `reports/results_and_discussion.md`.
- [x] **Threats to Validity & Security Analysis:** `reports/limitations.md`.
- [x] **IEEE-Style Research Paper (LaTeX Source):** `reports/ieee_research_paper.tex`.
- [x] **Authentic Bibliography:** `reports/references.bib`.
- [x] **Compiled Research Paper PDF:** `reports/ieee_research_paper.pdf`.
- [x] **Faculty Defense Presentation:** `reports/Blowfish_Benchmark_Presentation.pptx`.
- [x] **Viva Presentation Script & Speaker Notes:** `reports/presentation_script.md`.

---

## 3. Note on Machine Learning vs. Cryptographic Metrics

The collaborative R&D guideline template incorporates an evaluation module measuring ML classification metrics (Accuracy, Precision, Recall, F1-Score, ROC-AUC). As clarified in our research plan, machine learning classification metrics do not apply to symmetric block cipher evaluation. Instead, our study implements the direct cryptographic performance counterparts:
- **ML Training Latency $\longleftrightarrow$ Cryptographic Cipher Initialization & Subkey Expansion Latency (ms)**
- **ML Inference Latency per sample $\longleftrightarrow$ Cryptographic Steady-State Latency per block/MiB (ms)**
- **ML Classification Accuracy / F1 $\longleftrightarrow$ Cryptographic Round-Trip Decryption Correctness & SHA-256 Digest Integrity (100% Match)**
- **ML Model Parameter Memory $\longleftrightarrow$ Tracemalloc Heap & Operating System Process RSS Memory Footprint (MiB)**
- **Computational Efficiency $\longleftrightarrow$ Sustained Encryption/Decryption Throughput (MiB/s)**
