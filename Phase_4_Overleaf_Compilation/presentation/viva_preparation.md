# Faculty Presentation & Viva Defense Script

**Subject:** Cryptography and Network Security (CNS) A.Y. 2026–27  
**Faculty In-Charge:** Prof. Renuka Pawar  
**Institution:** Sardar Patel Institute of Technology (SPIT), Mumbai  
**Project:** The Flexible Variable-Key Block Cipher Framework (Blowfish)  
**Research Title:** *Variable Key Length Impacts on Memory Allocation and Throughput in Blowfish Cryptographic Frameworks*  

---

## Slide 1: Title & Collaborative R&D Overview
- **Visual:** Project title, Sardar Patel Institute of Technology header, CNS Course, Prof. Renuka Pawar, Student Names & Roll Numbers.
- **Spoken Defense Script:**
  > "Respected Prof. Renuka Pawar and faculty members, good afternoon. Today, our group presents our research on *'Variable Key Length Impacts on Memory Allocation and Throughput in Blowfish Cryptographic Frameworks'*. As part of the SPIT CNS Collaborative R&D Manifest, our goal is to move beyond textbook theoretical claims and provide an empirical, experimentally validated performance analysis of variable secret-key ciphers under rigorous scientific benchmarking standards."

---

## Slide 2: Problem Formulation & Research Motivation
- **Visual:** Block cipher comparison diagram (AES fixed 128/192/256 vs. Blowfish variable 32–448 bits), real-world applications in OpenVPN, disk encryption, and password hashing (bcrypt).
- **Spoken Defense Script:**
  > "Most contemporary standard ciphers—notably AES—mandate rigid, fixed key lengths. However, Bruce Schneier's Blowfish cipher introduced a flexible variable-key paradigm, supporting secret keys from 32 bits up to 448 bits. While cryptanalytic literature has extensively evaluated its resistance to differential cryptanalysis, there is a distinct lack of empirical performance data quantifying how variable key lengths impact initialization latency, steady-state throughput, and memory consumption. Our project systematically tests these dynamics."

---

## Slide 3: Blowfish Algorithmic Architecture & Key Expansion
- **Visual:** 16-round Feistel architecture diagram; $F$-function arithmetic; mathematical subkey expansion cycle showing $P$-array (18 entries) and four $S$-boxes (1,024 entries).
- **Spoken Defense Script:**
  > "To understand our experimental findings, we must examine the internal mechanics of Blowfish. Blowfish uses a 16-round Feistel structure on 64-bit blocks. Crucially, its subkey expansion works in two stages:
  > First, the 18 $P$-array entries and four 256-entry $S$-boxes are loaded with fractional digits of $\pi$.
  > Second, the user's secret key is cyclically XORed across the $P$-array, followed by **521 iterative block encryptions** using Blowfish itself to generate all subkeys.
  > This architecture leads directly to our core scientific hypothesis: Because 521 encryptions are executed regardless of key length, steady-state memory and throughput should remain invariant across all key sizes from 32 to 448 bits!"

---

## Slide 4: Research Questions & Core Hypotheses
- **Visual:** Table of 5 research hypotheses ($H_1$ to $H_5$) with expected outcomes.
- **Spoken Defense Script:**
  > "We formulated five precise research hypotheses:
  > - **$H_1$:** Does secret key length measurably alter cipher initialization time?
  > - **$H_2$:** Does key length influence steady-state encryption throughput?
  > - **$H_3$:** How does input file size govern throughput amortization and latency?
  > - **$H_4$:** Does memory allocation scale with key length or input file size?
  > - **$H_5$:** Are observed performance variations statistically significant or merely microarchitectural noise?"

---

## Slide 5: Experimental Design & Benchmark Matrix
- **Visual:** Experimental factorial matrix table (14 keys × 5 file sizes × 13 repetitions = 1,820 trials); CBC mode with fresh 64-bit IV per trial; SHA-256 integrity verification.
- **Spoken Defense Script:**
  > "Our experimental matrix encompasses all 14 standard key lengths: from 32 bits up to 448 bits in 32-bit steps.
  > We evaluated five distinct binary workloads: 1 KiB, 100 KiB, 1 MiB, 10 MiB, and 50 MiB.
  > To ensure scientific validity, every configuration was subjected to 3 warm-up runs followed by 10 measured repetitions.
  > We enforced NIST SP 800-38A CBC mode with PKCS#7 padding, generating a fresh, cryptographically secure 64-bit IV for every single encryption.
  > Finally, 100% round-trip correctness was confirmed via automated SHA-256 hash comparisons."

---

## Slide 6: Experimental Findings: Cipher Initialization & Key Schedule
- **Visual:** Embedded Figure 1 (Key vs. Init Time with 95% CI) and Figure 2 (Initialization Variability & CV %).
- **Spoken Defense Script:**
  > "Turning to our empirical findings: Figure 1 plots cipher initialization time across all 14 key sizes. 
  > Notice that initialization requires approximately 0.04 to 0.08 milliseconds.
  > Our ANOVA and linear regression analysis confirms that key length produces no practically significant trend on initialization time. The 521 internal Feistel encryptions dominate the subkey generation pipeline, making the initial key-XORing phase negligible in overall initialization cost."

---

## Slide 7: Experimental Findings: Throughput & Latency Scaling
- **Visual:** Embedded Figure 3 (Encryption Throughput vs. File Size), Figure 4 (Decryption Throughput), and Figure 5 (Multi-panel Throughput across all 14 keys).
- **Spoken Defense Script:**
  > "Figures 3 and 4 present our most striking throughput findings:
  > For small 1 KiB files, throughput is amortized at ~10 to 15 MiB/s due to per-call invocation overhead.
  > As the payload increases to 100 KiB and 1 MiB, throughput rapidly surges and stabilizes at a steady-state plateau of **~130 to 145 MiB/s**.
  > Across all 14 key sizes—from 32 bits to 448 bits—throughput curves overlap almost perfectly. Figure 5 demonstrates this invariance across every payload size: steady-state encryption throughput is independent of secret key length!"

---

## Slide 8: Memory Profiling & Allocation Analysis
- **Visual:** Embedded Figure 8 (Memory vs. File Size: Heap vs. RSS) and Figure 9 (Memory Invariance vs. Key Length).
- **Spoken Defense Script:**
  > "In Figure 8 and 9, we examine memory consumption using dual-layer profiling: Python heap allocation via `tracemalloc` and process-level RSS via `psutil`.
  > Heap memory scales strictly with input payload size because memory is allocated for the plaintext and ciphertext buffers.
  > However, as seen in Figure 9, key length has zero impact on memory footprint. Blowfish's internal expanded subkey state—18 P-array words and 1,024 S-box entries—occupies exactly 4,168 bytes, which remains completely constant regardless of input key length."

---

## Slide 9: Cryptographic Security & Limitations (The Sweet32 Attack)
- **Visual:** Birthday bound collision diagram; Sweet32 attack parameters ($2^{32}$ blocks = 32 GiB); lack of authentication in CBC mode.
- **Spoken Defense Script:**
  > "A critical responsibility of cybersecurity researchers is recognizing cryptographic limitations:
  > First, Blowfish uses a 64-bit block size. Under the Birthday Paradox, ciphertext collisions occur with 50% probability after encrypting $2^{32}$ blocks—which is only **32 GiB** under a single key. In 2016, the Sweet32 attack by Bhargavan and Leurent proved this vulnerability practically breaks TLS and OpenVPN.
  > Second, CBC mode provides confidentiality but not authenticity. For production security, modern systems must migrate to 128-bit AEAD ciphers like AES-GCM or ChaCha20-Poly1305.
  > We emphasize that our 100% round-trip pass rate confirms functional correctness, not mathematical immunity to cryptanalysis."

---

## Slide 10: Conclusion & Collaborative R&D Compliance
- **Visual:** Summary of validated answers to all 5 research questions; SPIT CNS 4-week timeline completion; QR code/link to repository and IEEE paper.
- **Spoken Defense Script:**
  > "To conclude:
  > 1. Secret key length does not impair steady-state throughput or memory footprint in Blowfish.
  > 2. Throughput is governed primarily by workload size, reaching saturation at ~140 MiB/s for workloads $\ge 1\text{ MiB}$.
  > 3. Blowfish initialization is dominated by 521 self-encryptions.
  > 4. All 1,820 experimental trials passed 100% cryptographic integrity checks.
  > All deliverables—source code, raw datasets, 12 IEEE figures, LaTeX manuscript, and presentation—are fully completed in compliance with Prof. Renuka Pawar's syllabus requirements. We are now open for questions. Thank you."

---

## Anticipated Faculty Viva Questions & Model Answers

### Q1: Why did you not report Accuracy, Precision, Recall, or F1-score as shown in the tournament evaluation code in the PDF?
**Answer:**
"The evaluation module in the faculty manifest was provided as a generic template for machine learning classifiers (supervised/unsupervised). In symmetric cryptography, block ciphers are deterministic mathematical permutations, not probabilistic classification models. Reporting classification accuracy would be scientifically invalid. Instead, we mapped those requirements directly to cryptographic counterparts: Training time corresponds to Key-Schedule Initialization Latency, Inference time corresponds to Encryption Latency per MiB, and Classification Accuracy is replaced by 100% SHA-256 Round-Trip Integrity Verification."

### Q2: Why is steady-state encryption throughput identical for a 32-bit key and a 448-bit key?
**Answer:**
"Because Blowfish decouples key expansion from block encryption. The secret key is only used during initialization to seed the subkeys. Once the 18 P-array subkeys and four S-boxes are populated in memory, the 16-round Feistel transformation executes the exact same mathematical operations—16 XORs, 16 additions mod $2^{32}$, and 16 table lookups—regardless of how long the original key was."

### Q3: What is the Sweet32 vulnerability and why does it affect Blowfish?
**Answer:**
"The Sweet32 vulnerability stems from Blowfish's 64-bit block size. In CBC mode, ciphertext collisions begin occurring after $2^{n/2} = 2^{32}$ blocks, which equals 32 GiB of data. In 2016, Bhargavan and Leurent demonstrated that an active eavesdropper on a long-lived TLS or OpenVPN session can exploit these collisions to recover plaintext session cookies. This is why NIST and modern standards deprecated 64-bit ciphers in favor of 128-bit ciphers like AES."

### Q4: What is the difference between tracemalloc and psutil in your memory measurements?
**Answer:**
"`tracemalloc` tracks Python-level heap allocations, measuring the memory Python explicitly allocates for byte buffers and objects. However, PyCryptodome's Blowfish core is implemented in compiled C, which allocates memory outside the Python runtime. `psutil` measures whole-process Resident Set Size (RSS) at the OS level, capturing the C library footprint, but it is subject to Windows page faulting and runtime noise. We reported both independently to ensure transparency."
