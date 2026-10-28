# Final Submission Status & Provenance Record

**Course:** Cryptography and Network Security (CNS) A.Y. 2026–27  
**Faculty In-Charge:** Prof. Renuka Pawar  
**Institution:** Sardar Patel Institute of Technology (SPIT), Mumbai  
**Project:** The Flexible Variable-Key Block Cipher Framework (Blowfish)  
**Research Investigation:** *Variable Key Length Impacts on Memory Allocation and Throughput in Blowfish Cryptographic Frameworks*  
**Student Lead:** Rutuja Hirudkar  

---

## 1. Deliverables Copy & Provenance Mapping
As mandated by the strict output management policy, all deliverables in this folder are **verified copies** of outputs produced in earlier phases. The original files remain intact in their respective phase directories.

| Deliverable in `FINAL_SUBMISSION/` | Source Phase & Canonical Path | Verification Gate Passed | Size | Status |
| :--- | :--- | :---: | :---: | :---: |
| `model_script.py` | `Phase_3_Tournament_Benchmark/src/model_script.py` | Phase 3 Gate | 4.9 KB | **VERIFIED COPY** |
| `final_benchmark_summary.csv` | `Phase_3_Tournament_Benchmark/processed_data/benchmark_summary.csv` | Phase 3 Gate | 31.8 KB | **VERIFIED COPY** |
| `final_report.pdf` | `Phase_4_Overleaf_Compilation/paper/paper.pdf` | Phase 4 Gate | 1.05 MB | **VERIFIED COPY** |
| `presentation.pptx` | `Phase_4_Overleaf_Compilation/presentation/presentation.pptx` | Phase 4 Gate | 824 KB | **VERIFIED COPY** |
| `ieee_research_paper.tex` | `Phase_4_Overleaf_Compilation/paper/ieee_research_paper.tex` | Phase 4 Gate | 19.8 KB | **VERIFIED COPY** |
| `references.bib` | `Phase_4_Overleaf_Compilation/paper/references.bib` | Phase 4 Gate | 1.8 KB | **VERIFIED COPY** |
| `graphs/fig01_key_vs_init_time.png` | `Phase_3_Tournament_Benchmark/graphs/fig01_key_vs_init_time.png` | Phase 3 Gate | 185 KB | **VERIFIED COPY** |
| `graphs/fig02_init_time_variability.png` | `Phase_3_Tournament_Benchmark/graphs/fig02_init_time_variability.png` | Phase 3 Gate | 215 KB | **VERIFIED COPY** |
| `graphs/fig03_enc_throughput_vs_size.png` | `Phase_3_Tournament_Benchmark/graphs/fig03_enc_throughput_vs_size.png` | Phase 3 Gate | 224 KB | **VERIFIED COPY** |
| `graphs/fig04_dec_throughput_vs_size.png` | `Phase_3_Tournament_Benchmark/graphs/fig04_dec_throughput_vs_size.png` | Phase 3 Gate | 228 KB | **VERIFIED COPY** |
| `graphs/fig05_key_vs_throughput_panels.png` | `Phase_3_Tournament_Benchmark/graphs/fig05_key_vs_throughput_panels.png` | Phase 3 Gate | 265 KB | **VERIFIED COPY** |
| `graphs/fig06_enc_latency_vs_size.png` | `Phase_3_Tournament_Benchmark/graphs/fig06_enc_latency_vs_size.png` | Phase 3 Gate | 212 KB | **VERIFIED COPY** |
| `graphs/fig07_dec_latency_vs_size.png` | `Phase_3_Tournament_Benchmark/graphs/fig07_dec_latency_vs_size.png` | Phase 3 Gate | 214 KB | **VERIFIED COPY** |
| `graphs/fig08_memory_vs_file_size.png` | `Phase_3_Tournament_Benchmark/graphs/fig08_memory_vs_file_size.png` | Phase 3 Gate | 208 KB | **VERIFIED COPY** |
| `graphs/fig09_memory_vs_key_length.png` | `Phase_3_Tournament_Benchmark/graphs/fig09_memory_vs_key_length.png` | Phase 3 Gate | 242 KB | **VERIFIED COPY** |
| `graphs/fig10_normalized_performance.png` | `Phase_3_Tournament_Benchmark/graphs/fig10_normalized_performance.png` | Phase 3 Gate | 236 KB | **VERIFIED COPY** |
| `graphs/fig11_key_size_heatmap.png` | `Phase_3_Tournament_Benchmark/graphs/fig11_key_size_heatmap.png` | Phase 3 Gate | 288 KB | **VERIFIED COPY** |
| `graphs/fig12_correctness_summary.png` | `Phase_3_Tournament_Benchmark/graphs/fig12_correctness_summary.png` | Phase 3 Gate | 134 KB | **VERIFIED COPY** |

---

## 2. Institutional Compliance Checklist
- [x] **No Inter-Phase Data Pollution:** Pilot data remains strictly in `Phase_2_Local_Tuning/pilot_results/`. Tournament benchmark data resides strictly in `Phase_3_Tournament_Benchmark/`.
- [x] **Deterministic Data Lock:** 5 binary workloads frozen in `Phase_1_Data_Lock/test_data/` with verified SHA-256 digests.
- [x] **Audited Warm-Up Policy:** 5 pre-warmup runs applied to key schedule, eliminating cold-start latency artifacts.
- [x] **Five-Workload Throughput Reconciled:** All five workload sizes (1 KiB, 100 KiB, 1 MiB, 10 MiB, 50 MiB) present in Table II.
- [x] **Three-Tier Memory Architecture:** Theoretical subkeys (4,168 B), Python heap (tracemalloc), and Process RSS (psutil) explicitly delineated.
- [x] **Authentic Bibliography:** 100% bijective match between LaTeX `\cite{}` commands and `references.bib`.
- [x] **Reproducible Executables:** `Phase_3_Tournament_Benchmark/src/tournament_benchmark.py`, `compile_paper_pdf.py`, and `generate_presentation.py` runnable locally without external server dependencies.

Sign-off: Rutuja Hirudkar (Student Lead) & Prof. Renuka Pawar (Faculty Supervisor).
