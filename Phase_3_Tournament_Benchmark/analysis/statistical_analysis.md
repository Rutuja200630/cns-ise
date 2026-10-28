# Phase 3: Formal Statistical Analysis & Hypothesis Testing

**Course:** Cryptography and Network Security (CNS) A.Y. 2026–27  
**Faculty In-Charge:** Prof. Renuka Pawar  
**Institution:** Sardar Patel Institute of Technology, Mumbai  
**Topic:** *Variable Key Length Impacts on Memory Allocation and Throughput in Blowfish Cryptographic Frameworks*  

---

## 1. Statistical Methodology & Data Cleaning
- **Raw Observations (N):** 1,820 individual trials (14 key lengths $\times$ 5 file sizes $\times$ 13 repetitions $\times$ 2 operations).
- **Warm-Up Exclusion:** 420 warm-up runs (3 per configuration) flagged with `is_warmup=True` were excluded to prevent cold-start cache and memory allocation bias.
- **Valid Measured Sample:** 1,400 trials ($14 \times 5 \times 10 \times 2$).
- **Key-Schedule Observations:** 420 initialization runs (30 per key length across all 14 key sizes).
- **Confidence Intervals:** 95% Confidence Intervals computed via Student's $t$-distribution:
  $$\text{CI}_{95\%} = \bar{x} \pm t_{0.025, N-1} \cdot \frac{s}{\sqrt{N}}$$

---

## 2. Hypothesis 1: Key Length Impact on Cipher Initialization Latency

- **Null Hypothesis ($H_{0,1}$):** Secret key length does not affect cipher initialization time.
- **Alternative Hypothesis ($H_{a,1}$):** Longer secret keys require statistically significantly more initialization time.

### Parametric Test (One-Way ANOVA across 14 Key Sizes):
- **$F$-statistic:** $1.4023$
- **$p$-value:** $0.1548$ ($p > 0.05$)
- **Verdict:** Fail to reject $H_{0,1}$. The differences in cipher initialization latency across the 14 key sizes are statistically insignificant.

### Non-Parametric & Regression Verification:
- **Linear Regression:**
  - Slope: $-0.00021\text{ ms/bit}$
  - $R^2$: $0.0051$ ($p = 0.1444$)
  - Interpretation: Key length accounts for less than **0.51%** of variance in initialization time.
- **Algorithmic Explanation:**
  The subkey expansion executes 18 cyclic XOR operations followed by **521 iterative block encryptions** to populate the 18 P-array entries and 1,024 S-box entries. The 521 encryptions consume $>99.5\%$ of the total initialization budget, rendering the length of the secret key (4 to 56 bytes) statistically negligible.

---

## 3. Hypothesis 2: Key Length Impact on Steady-State Throughput

- **Null Hypothesis ($H_{0,2}$):** Steady-state throughput is invariant to secret key length once subkeys are initialized.
- **Alternative Hypothesis ($H_{a,2}$):** Longer secret keys reduce steady-state throughput.

### ANOVA Results by Workload Size:
- **1 KiB:** $F = 14.91, p = 8.00 \times 10^{-20}$ (Mean TP: $\approx 15.6\text{--}17.0\text{ MiB/s}$)
- **100 KiB:** $F = 15.82, p = 9.02 \times 10^{-21}$ (Mean TP: $\approx 847\text{--}990\text{ MiB/s}$)
- **1 MiB:** $F = 69.11, p = 8.13 \times 10^{-51}$ (Mean TP: $\approx 109\text{--}121\text{ MiB/s}$)
- **10 MiB:** $F = 8.25, p = 7.92 \times 10^{-12}$ (Mean TP: $\approx 82\text{--}165\text{ MiB/s}$)
- **50 MiB:** $F = 28.12, p = 4.13 \times 10^{-31}$ (Mean TP: $\approx 100\text{--}213\text{ MiB/s}$)

### Practical vs. Statistical Significance Interpretation:
While high sample counts ($N=10$ per group, 140 total comparisons per workload) yield statistically significant $p$-values due to tiny standard errors, the **effect size is non-monotonic with respect to key length**. For example, at 50 MiB, the 448-bit key achieved the highest mean throughput (213.9 MiB/s) while the 384-bit key was 165.6 MiB/s and the 32-bit key was 104.1 MiB/s. These variations are driven by CPU dynamic frequency scaling (Intel Turbo Boost/SpeedStep) and thread context-switching in the host OS, not by the number of key bytes.

**Algorithmic Confirmation:** In all cases, 16 Feistel rounds are executed on 64-bit blocks. The Feistel function does not reference the original key, confirming operational invariance.

---

## 4. Hypothesis 3: Memory Allocation Invariance

- **Null Hypothesis ($H_{0,3}$):** Secret key length does not alter internal cipher memory footprint.
- **Finding:**
  At 50 MiB, peak Python heap memory (`tracemalloc`) across key lengths was:
  - 32-bit key: $176,711,295\text{ bytes}$
  - 128-bit key: $176,711,307\text{ bytes}$
  - 256-bit key: $176,711,321\text{ bytes}$
  - 448-bit key: $176,711,481\text{ bytes}$
  The difference across the entire 416-bit span is **186 bytes**, corresponding strictly to Python's internal byte array representation.
- Process RSS (`psutil`) remained constant at $265.6\text{ MiB}$.
- **Conclusion:** Subkey expansion maintains fixed internal state (4,168 bytes), proving memory invariance to key length.
