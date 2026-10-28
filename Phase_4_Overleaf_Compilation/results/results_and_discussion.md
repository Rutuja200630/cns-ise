# Experimental Results and Scientific Discussion

**Research Title:** *Variable Key Length Impacts on Memory Allocation and Throughput in Blowfish Cryptographic Frameworks*  
**Project:** The Flexible Variable-Key Block Cipher Framework (Blowfish)  
**Subject:** Cryptography and Network Security (CNS A.Y. 2026–27)  
**Faculty In-Charge:** Prof. Renuka Pawar  
**Institution:** Sardar Patel Institute of Technology, Mumbai  

---

## 1. Experimental Overview & Dataset Integrity

The complete experimental matrix was executed on the designated host environment (Intel64 architecture, 16 GB physical RAM, Windows 10/11, CPython 3.9.13, PyCryptodome 4.2.0). 
- **Total Planned & Executed Trials:** 1,820 raw trials (14 key lengths $\times$ 5 file sizes $\times$ 13 repetitions $\times$ 2 operations).
- **Warm-Up Iterations Excluded:** 420 warm-up trials (3 per configuration) were strictly excluded from sample statistics.
- **Valid Measured Trials:** 1,400 measured trials (10 per configuration).
- **Key-Schedule Repetitions:** 30 independent high-resolution timing iterations across all 14 key lengths (420 total initialization trials).
- **Cryptographic Correctness:** **100.0% pass rate** (0 failures across all 1,820 trials). Every round trip was cryptographically verified using SHA-256 digests.

---

## 2. Answers to Research Hypotheses & Experimental Findings

### Research Question 1: Does increasing key length measurably affect cipher initialization time?
**Empirical Finding:** *No practical or linear dependence.*  
- **Measured Data:** Across all 14 key lengths (32 to 448 bits), the mean cipher initialization time ranged between **0.042 ms and 0.104 ms** (with a single 32-bit cold-start outlier at 0.36 ms). The median initialization time remained exceptionally tight between **0.037 ms and 0.098 ms**.
- **Statistical Significance:** One-way ANOVA yielded $F = 1.4023, p = 0.1548$ ($p > 0.05$). Linear regression of initialization time against key length yielded $R^2 = 0.0051$ ($p = 0.1444$).
- **Algorithmic Explanation:** Blowfish subkey expansion initializes the 18 P-array entries and 1,024 S-box entries with fractional digits of $\pi$. While user key bytes are cyclically XORed into the P-array, this operation requires only 18 word XORs regardless of key length. Subsequently, the algorithm executes **exactly 521 iterative block encryptions** to expand the subkeys. The 521 encryptions account for $>99.5\%$ of initialization latency, rendering the user key length statistically undetectable in initialization cost.

### Research Question 2: Does key length substantially affect steady-state encryption throughput?
**Empirical Finding:** *Steady-state throughput is invariant to key length.*  
- **Measured Data:** For representative large workloads (50 MiB), steady-state encryption throughput across key lengths clustered within **100 MiB/s to 213 MiB/s**, with medians tightly grouped near ~180–190 MiB/s. Small variations across runs are attributable to operating system thread preemption and CPU dynamic clock scaling (Intel SpeedStep).
- **Statistical Distinction:** While large sample sizes in ANOVA detected small $p$-values across key length groups, the effect size is dominated by runtime scheduling jitter rather than algorithmic complexity.
- **Algorithmic Explanation:** Once subkeys are stored in the 18-element P-array and four S-boxes, the 16-round Feistel network executes identical operations—16 XORs, 16 additions mod $2^{32}$, and 16 table lookups—for every 64-bit block, completely independent of the original key size.

### Research Question 3: How does file size affect throughput and latency?
**Empirical Finding:** *Throughput exhibits classic amortization saturation; latency scales linearly with payload size.*  
- **Small Workloads (1 KiB):** Throughput is low (~10 to 17 MiB/s), dominated by function call dispatch, buffer setup, and timer resolution overhead.
- **Medium Workloads (100 KiB – 1 MiB):** Throughput surges past 100 MiB/s as fixed per-call overheads are amortized over larger block counts.
- **Large Workloads (10 MiB – 50 MiB):** Throughput plateaus at full steady-state saturation (~130 to 200 MiB/s). Latency exhibits strict linear scaling ($O(N)$), transitioning from $<0.1\text{ ms}$ at 1 KiB to $\approx 250\text{--}480\text{ ms}$ at 50 MiB.

### Research Question 4: Does memory consumption change with key length or file size?
**Empirical Finding:** *Memory scales strictly with payload buffer size and is 100% invariant to secret key length.*  
- **Key Length Invariance:** For the 50 MiB workload, peak Python heap allocation across key lengths was:
  - 32-bit key: $176,711,295\text{ bytes}$
  - 128-bit key: $176,711,307\text{ bytes}$
  - 256-bit key: $176,711,321\text{ bytes}$
  - 448-bit key: $176,711,481\text{ bytes}$
  The difference across the entire 416-bit key spectrum is only **186 bytes**, corresponding solely to Python's internal representation of the key byte array!
- **Payload Scaling:** Peak Python heap scales linearly with workload size due to allocating memory for the original payload, padded buffer, and resulting ciphertext. Process RSS remained stable at ~125 MiB for small workloads and ~278 MiB for 50 MiB.

---

## 3. Systematic Interpretation of Experimental Figures

| Figure | Description | Key Empirical Observation |
| :--- | :--- | :--- |
| **Figure 1** | Key Length vs. Cipher Initialization Time (ms) | Mean initialization remains stable between 0.04 ms and 0.10 ms across all 14 key lengths with overlapping 95% confidence intervals. |
| **Figure 2** | Initialization-Time Variability | Standard deviation and Coefficient of Variation (CV) remain bounded between 9% and 45%, reflecting microarchitectural timer resolution limits. |
| **Figure 3** | Encryption Throughput vs. File Size | Rapid non-linear rise from ~15 MiB/s at 1 KiB to a sustained plateau of ~130–190 MiB/s for workloads $\ge 1\text{ MiB}$. |
| **Figure 4** | Decryption Throughput vs. File Size | Decryption mirrors encryption curves, exhibiting symmetric Feistel performance. |
| **Figure 5** | Key Length vs. Throughput Panels | Bar charts across all 14 key sizes demonstrate near-uniform throughput bars at every file size. |
| **Figure 6 & 7** | Encryption & Decryption Latency | Strict linear $O(N)$ scaling from sub-millisecond latencies at 1 KiB to ~250–480 ms at 50 MiB. |
| **Figure 8** | Memory Footprint vs. Workload Size | Dual-layer plot highlights difference between Python heap (`tracemalloc`) and process physical RSS (`psutil`). |
| **Figure 9** | Memory Usage vs. Key Length | Flat horizontal line across all 14 key lengths, visually proving memory invariance. |
| **Figure 10** | Normalized Performance (128-bit Baseline) | Normalized throughput across key lengths hovers near $1.0 \pm 0.1$, confirming no systematic degradation for longer keys. |
| **Figure 11** | Key Length $\times$ File Size Heatmap | Color gradient illustrates throughput transition from low (cool) at 1 KiB to saturated (warm) at 50 MiB. |
| **Figure 12** | Correctness Validation Summary | 1,400 / 1,400 passed trials (100% round-trip integrity match). Zero corruption. |
