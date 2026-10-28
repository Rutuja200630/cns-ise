# Phase 3: Tournament Benchmark

**Phase:** Phase_3_Tournament_Benchmark  
**Milestone:** End of Week 3 (SPIT CNS Collaborative R&D Manifest)  
**Status:** **BENCHMARKED & VALIDATED**  

---

## Purpose
This phase contains the complete, production-grade tournament benchmark dataset, execution scripts, statistical hypothesis evaluations, data tables, and 12 publication-quality visualizations for the Blowfish variable-key cryptographic framework.

## Strict Directory Architecture
- `src/` — Standalone execution and evaluation code (`model_script.py`, `statistics_analysis.py`, `visualization.py`, `validate_results.py`).
- `raw_data/` — Individual timing and memory observations (`benchmark_raw.csv` [1,820 trials], `key_schedule_raw.csv` [420 trials], `memory_raw.csv`).
- `processed_data/` — Aggregated summary statistics across 140 configurations (`benchmark_summary.csv`, `key_schedule_results.csv`, `memory_summary.csv`).
- `graphs/` — 12 publication-quality 300 DPI figures (`fig01` to `fig12`).
- `tables/` — Markdown and CSV formatted tables of initialization latency, steady-state throughput, and memory footprint.
- `analysis/` — Formal hypothesis testing (`statistical_analysis.md`) and empirical discussion (`results_and_discussion.md`).
- `environment/` — Frozen host machine hardware and dependency snapshot (`environment_report.json`).
- `validation/` — Automated validation audit report (`validation_report.md` & `phase_3_validation.txt`).
- `deliverables_manifest.csv` — Comprehensive inventory of Phase 3 artifacts.

## Validation Gate
To re-verify the Phase 3 data and graph integrity:
```powershell
python Phase_3_Tournament_Benchmark/src/validate_results.py
```
*All 1,820 trials must show non-negative durations, zero correctness failures, and mathematical agreement between raw and summary files.*
