# The Flexible Variable-Key Block Cipher Framework (Blowfish)

### *Variable Key Length Impacts on Memory Allocation and Throughput in Blowfish Cryptographic Frameworks*

**Institution:** Sardar Patel Institute of Technology (SPIT), Munshi Nagar, Andheri (W), Mumbai-400058  
**Department:** Computer Engineering / Information Technology  
**Subject:** Cryptography and Network Security (CNS) A.Y. 2026–27  
**Faculty In-Charge:** Prof. Renuka Pawar  
**Collaborative Manifest:** Scopus/IEEE Tournament Benchmarking & Master Manuscript  
**Project Folder:** `cns ise/`  

---

## 1. Strict Phase-Wise Architecture

This repository strictly enforces phase-wise output management aligned with the 4-week timeline in Prof. Renuka Pawar's *Collaborative R&D Manifest: Comparative Algorithmic Analysis for Advanced Cybersecurity Domains*. **No outputs are dumped in common unmanaged directories; each phase strictly owns its outputs, logs, manifests, and validation gates.**

```text
cns ise/
│
├── README.md                           <- Master project documentation & quickstart
├── PROJECT_PROGRESS.md                 <- Phase gate audit dashboard & task tracking
├── requirements.txt                    <- Pinned dependencies for reproducible execution
├── .gitignore                          <- Standard version control exclusions
├── .gitattributes                      <- LF normalization and binary attributes
├── model_script.py                     <- Standalone tournament evaluation engine
│
├── Phase_1_Data_Lock/                  <- Week 1: Data Lock & Pipeline Integrity
│   ├── README.md                       <- Phase 1 overview and usage
│   ├── project_requirements.md         <- Institutional and cipher specifications
│   ├── experiment_config.json          <- Locked benchmark parameters (14 keys, 5 sizes)
│   ├── environment_info.json           <- Frozen machine specs (Intel64, Windows, RAM)
│   ├── test_file_manifest.csv          <- Locked test file table with SHA-256 hashes
│   ├── test_data/                      <- 5 exact binary test workloads (1 KiB to 50 MiB)
│   ├── logs/                           <- Phase 1 execution logs
│   ├── validation/                     <- Phase 1 audit sign-off (phase_1_validation.txt)
│   └── deliverables_manifest.csv       <- Inventory of Phase 1 artifacts
│
├── Phase_2_Local_Tuning/               <- Week 2: Local Tuning & Parameter Sprints
│   ├── README.md                       <- Phase 2 overview and tuning decisions
│   ├── src/                            <- Core engine (blowfish_engine.py, benchmark.py, memory_profiler.py)
│   ├── tests/                          <- Automated test suite (14 passing unit tests)
│   ├── pilot_results/                  <- ISOLATED pilot tuning CSVs (pilot_raw.csv, pilot_summary.csv)
│   ├── analysis/                       <- Parameter comparison matrix (parameter_comparison.csv)
│   ├── methodology/                    <- Mathematical proof (key_schedule_explanation.md)
│   ├── logs/                           <- Phase 2 tuning and pytest logs
│   ├── validation/                     <- Phase 2 audit sign-off (phase_2_validation.txt)
│   └── deliverables_manifest.csv       <- Inventory of Phase 2 artifacts
│
├── Phase_3_Tournament_Benchmark/       <- Week 3: Tournament Benchmark Sync
│   ├── README.md                       <- Phase 3 overview and benchmark architecture
│   ├── src/                            <- Tournament scripts (model_script.py, statistics, viz, validate)
│   ├── raw_data/                       <- 1,820 individual timing trials (benchmark_raw.csv, key_schedule_raw.csv, memory_raw.csv)
│   ├── processed_data/                 <- Aggregated metrics across 140 configs (benchmark_summary.csv, key_schedule_results.csv, memory_summary.csv)
│   ├── graphs/                         <- 12 High-Resolution 300 DPI research figures (fig01 to fig12)
│   ├── tables/                         <- CSV and markdown data tables for paper insertion
│   ├── analysis/                       <- Formal hypothesis tests (statistical_analysis.md) and discussion
│   ├── environment/                    <- Frozen host runtime snapshot (environment_report.json)
│   ├── logs/                           <- Tournament execution logs
│   ├── validation/                     <- Automated audit report (validation_report.md & phase_3_validation.txt)
│   └── deliverables_manifest.csv       <- Inventory of Phase 3 artifacts
│
├── Phase_4_Overleaf_Compilation/       <- Week 4: Overleaf Compilation & Cross-Review
│   ├── README.md                       <- Phase 4 overview and Overleaf sync guide
│   ├── paper/                          <- IEEEtran LaTeX paper (ieee_research_paper.tex), bibliography (references.bib), and compiled PDF (paper.pdf [1.83 MB])
│   ├── figures/                        <- Verified copies of all 12 Phase 3 figures
│   ├── tables/                         <- Verified copies of benchmark data tables
│   ├── results/                        <- Written results discussion text
│   ├── presentation/                   <- 10-slide PowerPoint deck (presentation.pptx [1.39 MB]) & viva defense guide (viva_preparation.md)
│   ├── review/                         <- Multi-author cross-review and Turnitin checklist (<15% target)
│   ├── logs/                           <- Build and compilation logs
│   ├── validation/                     <- Phase 4 audit sign-off (phase_4_validation.txt)
│   └── deliverables_manifest.csv       <- Inventory of Phase 4 artifacts
│
├── FINAL_SUBMISSION/                   <- Verified Copies of Final Deliverables
│   ├── model_script.py                 <- Standalone tournament model script
│   ├── final_benchmark_summary.csv     <- Aggregated summary dataset
│   ├── graphs/                         <- Complete set of 12 research figures
│   ├── ieee_research_paper.tex         <- Full IEEEtran LaTeX source
│   ├── references.bib                  <- Authentic BibTeX citations
│   ├── final_report.pdf                <- Publication-ready compiled PDF manuscript (1.83 MB)
│   ├── presentation.pptx               <- 10-slide PowerPoint presentation with speaker notes (1.39 MB)
│   ├── README.md                       <- Final submission overview
│   ├── faculty_submission_checklist.md <- Complete manifest audit checklist
│   └── submission_status.md            <- Provenance record mapping files to source phases
│
└── git_docs/                           <- Git Version Control & Backup Records
    ├── git_workflow.md                 <- Commit conventions and remote push guide
    └── backup_status.md                <- Local disk backup verification
```

---

## 2. Quick Execution Guide (Windows PowerShell)

```powershell
# Navigate into the project root
cd "c:\Users\Rutuja Hirudkar\OneDrive\c\amazon\cns ise"

# 1. Run unit tests
python -m pytest Phase_2_Local_Tuning/tests/

# 2. Run the standardized tournament evaluation script
python model_script.py

# 3. Verify Phase 3 data integrity and validation audit
python Phase_3_Tournament_Benchmark/src/validate_results.py

# 4. View final submission deliverables
Get-ChildItem FINAL_SUBMISSION/
```

---

## 3. Key Empirical Findings (Summary of Validated Results)

All data was measured on an Intel64 host running Windows 10/11 with 16 GB RAM and PyCryptodome 4.2.0:
- **Cipher Initialization Latency is Invariant to Key Length:** Across all 14 key sizes, mean initialization time remained tightly bounded between **0.042 ms and 0.104 ms** (ANOVA $F = 1.4023, p = 0.1548 > 0.05$; linear regression $R^2 = 0.0051$). Blowfish subkey expansion is dominated by **521 iterative block encryptions**, rendering initial key-XOR differences undetectable in practice.
- **Steady-State Throughput is Invariant to Key Length:** Throughput plateaus at **~130 to 195 MiB/s** for workloads $\ge 1\text{ MiB}$ across all 14 key lengths from 32 to 448 bits. Once subkeys are stored in the 18 P-array entries and four S-boxes, the 16-round Feistel transformation executes the identical sequence of operations for every 64-bit block.
- **Memory Allocation is Invariant to Key Length:** At 50 MiB, peak Python heap memory differed by only **186 bytes** between a 32-bit key and a 448-bit key (due purely to Python byte array representation). Blowfish expanded subkeys occupy a constant **4,168 bytes** in memory.
- **Cryptographic Correctness:** **100% pass rate** across all 1,820 experimental trials. Every round trip was cryptographically verified via SHA-256 digests.
- **Security Limitation (The Sweet32 Attack):** Blowfish's 64-bit block size exposes it to collision attacks in CBC mode after encrypting $2^{32}$ blocks (**32 GiB**) under a single key (Bhargavan & Leurent, ACM CCS 2016). Blowfish is therefore deprecated for large data streams.
