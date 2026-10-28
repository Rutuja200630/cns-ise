# Phase 1: Data Lock & Pipeline Integrity

**Phase:** Phase_1_Data_Lock  
**Milestone:** End of Week 1 (SPIT CNS Collaborative R&D Manifest)  
**Status:** **LOCKED & VALIDATED**  

---

## Purpose
This phase establishes the foundational data arrays, test payload binaries, environment profiles, and cryptographic baseline hashes required for the Blowfish variable-key performance tournament.

## Deliverables in this Folder
1. `README.md` — Phase 1 guide and overview.
2. `project_requirements.md` — Complete specification of institutional and cryptographic constraints.
3. `experiment_config.json` — Immutable configuration defining 14 key sizes, 5 workloads, and benchmark repetitions.
4. `environment_info.json` — Machine specifications (Intel64, Windows 10, 16 GB RAM, Python 3.9.13, PyCryptodome 4.2.0).
5. `test_file_manifest.csv` — Table of verified test payloads, byte lengths, and SHA-256 digests.
6. `test_data/` — 5 deterministic test payload binary files (1 KiB, 100 KiB, 1 MiB, 10 MiB, 50 MiB).
7. `validation/phase_1_validation.txt` — Formal audit sign-off certifying Data Lock gate completion.
8. `deliverables_manifest.csv` — Comprehensive inventory of Phase 1 artifacts.

## Validation Gate
To verify Phase 1 data lock integrity at any time, ensure:
- All 5 test files exist in `test_data/` with exact byte counts.
- Recomputed SHA-256 digests match `test_file_manifest.csv` with zero divergence.
- Environment variables match `environment_info.json`.
