# Phase 4: Comprehensive Faculty Viva Preparation Guide

**Course:** Cryptography and Network Security (CNS) A.Y. 2026–27  
**Faculty In-Charge:** Prof. Renuka Pawar  
**Institution:** Sardar Patel Institute of Technology (SPIT), Mumbai  
**Project:** The Flexible Variable-Key Block Cipher Framework (Blowfish)  
**Topic:** *Variable Key Length Impacts on Memory Allocation and Throughput in Blowfish Cryptographic Frameworks*  
**Student Lead:** Rutuja Hirudkar  

---

## 1. Core Architectural Questions

### Q1: Why did you choose Blowfish to study variable-key behavior?
**Answer:** Blowfish is one of the very few symmetric block ciphers with an officially specified variable key length spanning an enormous range—from 32 bits up to 448 bits in 32-bit increments (14 standard sizes). Most modern ciphers (e.g., AES) only support 2 or 3 discrete key lengths (128, 192, 256 bits). Blowfish's wide 14-point parameter grid allows rigorous statistical modeling (ANOVA, regression) across key lengths to investigate if longer keys degrade performance.

### Q2: Why does Blowfish steady-state throughput remain invariant to secret key length?
**Answer:** Once the cipher is initialized, the secret key is never referenced again during block encryption. Instead, the 16-round Feistel network operates exclusively on the pre-computed 18-entry P-array and four 256-entry S-boxes. For every 64-bit block, the cipher executes identical operations: 16 XORs, 16 additions modulo $2^{32}$, and 16 table lookups—regardless of whether the key was 32 bits or 448 bits.

---

## 2. Experimental Audit & Warm-Up Policy Questions

### Q3: In baseline testing, the first 32-bit key measurement registered ~7.88 ms while other keys registered ~0.08 ms. Why did this happen and how was it audited?
**Answer:** This was an unmeasured cold-start artifact caused by the runtime environment:
1. Dynamic linking and loading of the PyCryptodome C extension DLL (`.pyd`) on the very first invocation.
2. Initial kernel page faults allocating text and data pages into physical RAM.
3. CPU frequency scaling (Intel SpeedStep) transitioning from low-power idle to full clock frequency.
Because the benchmark loop iterated sequentially starting at 32-bit (index 0), all cold-start overhead was captured solely in trial 1 of the 32-bit key.  
**Audit & Resolution:** We implemented a documented 5-iteration warm-up policy per key size, flagged with `is_warmup=True`. Discarding these warm-up runs reduced the 32-bit steady-state mean to **0.0896 ms** with a standard deviation of **0.0302 ms** (CV: 33.7%), fully aligned with all other 13 key lengths (0.056–0.162 ms).

### Q4: How many total trials were planned and executed in Phase 3?
**Answer:**
- **Steady-State Benchmark Trials:** 14 key sizes $\times$ 5 workloads (1 KiB, 100 KiB, 1 MiB, 10 MiB, 50 MiB) $\times$ 2 operations (encryption/decryption) $\times$ 13 repetitions (3 warm-ups + 10 measured) = **1,820 total trials** (recorded in `raw_data/benchmark_raw.csv`).
- **Key-Schedule Latency Trials:** 14 key sizes $\times$ 35 repetitions (5 warm-ups + 30 measured) = **490 total trials** (recorded in `raw_data/key_schedule_raw.csv`).
- **Summary Configurations:** Exactly 140 factorial test configurations ($14 \times 5 \times 2$).
- **Integrity Pass Rate:** 100.0% (zero failures across all 1,820 trials verified by SHA-256 round-trip digests).

---

## 3. Memory Hierarchy & Three-Tier Model Questions

### Q5: How do you separate theoretical subkey storage from measured Python heap memory and process RSS?
**Answer:** We established an explicit three-tier memory model:
1. **Tier 1 (Theoretical Subkey State):** 18 P-array words ($18 \times 4 = 72$ bytes) plus four 256-word S-boxes ($4 \times 256 \times 4 = 4,096$ bytes). Total internal algorithmic state is mathematically fixed at **4,168 bytes**, completely invariant to key size.
2. **Tier 2 (Python Runtime Heap via `tracemalloc`):** Tracks user-space Python objects (input byte arrays, PKCS#7 padding, output ciphertext). For a 50 MiB payload, peak heap is $\approx 168.52$ MiB. The difference between a 32-bit key and a 448-bit key is only **186 bytes** ($<0.0001\%$), attributable solely to Python `bytes` object header overhead.
3. **Tier 3 (Operating System Process RSS via `psutil`):** Measures physical RAM pages mapped into the process working set ($\approx 265.6$ MiB). This captures the Python VM, shared libraries, and OS allocator pools, remaining strictly constant across all key sizes.

---

## 4. Workload Scaling & Throughput Questions

### Q6: Why did the 100 KiB workload achieve the highest throughput (~371–702 MiB/s) compared to 10 MiB and 50 MiB (~83–214 MiB/s)?
**Answer:** This reflects CPU cache hierarchy and memory bus bandwidth:
- At 100 KiB, the entire plaintext, ciphertext, and subkey arrays fit completely within the CPU's high-speed L2/L3 cache (typically 512 KiB to 8 MiB per core), allowing execution at near-register memory bus speeds.
- At 10 MiB and 50 MiB, data spills beyond CPU cache into physical RAM, bottlenecking throughput at the system DDR4/DDR5 bus speed (~83–214 MiB/s).
- At 1 KiB, throughput drops to ~6.3–15.9 MiB/s due to Python-to-C dispatch call overhead and timer granularity.

---

## 5. Security & Practical Deployment Questions

### Q7: If Blowfish supports 448-bit keys, why is it deprecated in modern protocols?
**Answer:** Because of its **64-bit block size** ($b = 64$). Under the Birthday Paradox, a collision between two ciphertext blocks occurs with $p \ge 0.5$ once $2^{b/2} = 2^{32}$ blocks ($\approx 32$ GiB) are encrypted under a single key. The **Sweet32 attack** (Bhargavan & Leurent, ACM CCS 2016) demonstrated that an eavesdropper monitoring an HTTPS or OpenVPN stream can exploit collisions to extract plaintext authentication cookies. Increasing the key to 448 bits does NOT fix this block collision vulnerability; protocols must transition to 128-bit block ciphers like AES.
