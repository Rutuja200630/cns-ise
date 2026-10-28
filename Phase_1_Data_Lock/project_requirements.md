# Phase 1: Project Requirements & Institutional Data Lock Specification

**Course:** Cryptography and Network Security (CNS) A.Y. 2026–27  
**Faculty In-Charge:** Prof. Renuka Pawar  
**Institution:** Sardar Patel Institute of Technology (SPIT), Mumbai  
**Research Title:** *Variable Key Length Impacts on Memory Allocation and Throughput in Blowfish Cryptographic Frameworks*  

---

## 1. Institutional Framework Alignment (Collaborative R&D Manifest)
This phase satisfies **Milestone 1: Data Lock & Pipeline Integrity (End of Week 1)** from the SPIT Collaborative R&D Manifest.
- **Objective:** Form the unified, unshakeable empirical foundation across the batch.
- **Data Foundation Policy:** Deterministic binary payloads generated under reproducible cryptographic seeds.
- **Cryptographic Grounding:** Whereas machine learning tournament teams utilize standardized train-test splits ($X_{\text{train}}, X_{\text{test}}, y_{\text{train}}, y_{\text{test}}$), our cryptographic cipher tournament mandates standardized binary workload matrices ($1\text{ KiB}$ to $50\text{ MiB}$) with pre-locked cryptographic SHA-256 digests.

---

## 2. Parameter Matrix & Boundaries
- **Supported Key Lengths:** Exactly 14 key sizes: 32, 64, 96, 128, 160, 192, 224, 256, 288, 320, 352, 384, 416, 448 bits (4 to 56 bytes in 4-byte increments).
- **Supported Workloads:** 1 KiB, 100 KiB, 1 MiB, 10 MiB, 50 MiB.
- **Operational Standard:** NIST SP 800-38A CBC mode with PKCS#7 padding and fresh 64-bit random IV per trial.
- **Trial Structure:** 3 warm-ups + 10 measured repetitions = 13 iterations per configuration ($14 \times 5 \times 13 \times 2 = 1,820$ raw trials).

---

## 3. Data Integrity & Verification Protocol
1. Every test file has an exact byte length conforming to the power-of-two binary definition ($1\text{ KiB} = 1,024\text{ B}$, $1\text{ MiB} = 1,048,576\text{ B}$).
2. All files are 64-bit block-aligned before padding to evaluate clean block cipher boundaries.
3. Baseline SHA-256 digests are permanently locked in `test_file_manifest.csv`.
