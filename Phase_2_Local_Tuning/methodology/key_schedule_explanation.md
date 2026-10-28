# Phase 2: Mathematical Specification of Blowfish Key Scheduling & Feistel Rounds

**Course:** Cryptography and Network Security (CNS) A.Y. 2026–27  
**Faculty In-Charge:** Prof. Renuka Pawar  
**Institution:** Sardar Patel Institute of Technology, Mumbai  

---

## 1. Mathematical Structure of Blowfish Key Expansion

The core algorithmic uniqueness of Blowfish lies in its **subkey generation mechanism**, which operates as a pseudo-random bit generator seeded by the fractional digits of $\pi$ and modified by the secret key.

### Step 1: Initial Constant Seeding
The 18-element P-array and four 256-entry S-boxes are loaded with fixed hexadecimal constants from the fractional expansion of $\pi$:
$$P_1 = \text{0x243F6A88}, \quad P_2 = \text{0x85A308D3}, \quad \dots, \quad P_{18} = \text{0x8979FB1B}$$
$$S_{1,0} = \text{0xD1310BA6}, \quad \dots, \quad S_{4,255} = \text{0x8EFE3391}$$

### Step 2: Cyclic Key XOR
For an arbitrary secret key $K$ of length $k$ bytes ($4 \le k \le 56$, representing 32 to 448 bits), the key bytes are partitioned into 32-bit words and cyclically XORed into the 18 P-array entries:
$$P_i = P_i \oplus K_{(i-1) \pmod{k_{\text{words}}}} \quad \text{for } i = 1, 2, \dots, 18$$

### Step 3: Iterative Self-Encryption
An all-zero 64-bit block is encrypted using Blowfish with the state resulting from Step 2:
$$C_1 = \text{Blowfish}_{\text{Encrypt}}(\text{0x0000000000000000})$$
The resulting 64-bit ciphertext replaces $P_1$ and $P_2$:
$$P_1 = C_{1,\text{Left}}, \quad P_2 = C_{1,\text{Right}}$$
$C_1$ is then re-encrypted with the updated subkey state to produce $C_2$, which replaces $P_3$ and $P_4$. This process continues sequentially:
- Encrypting 9 times replaces all 18 entries of the P-array ($9 \times 2 = 18$).
- Encrypting 512 times replaces all 1,024 entries of the four S-boxes ($512 \times 2 = 1,024$).

$$\text{Total Subkey Encryptions} = 9 + 512 = 521 \text{ block encryptions}$$

---

## 2. Invariance Proof & Tuning Hypothesis

1. **Subkey Storage Invariance:**
   Regardless of whether the secret key is 32 bits (4 bytes) or 448 bits (56 bytes), the allocated storage for subkeys is identically:
   $$\text{Storage} = (18 \times 4) + (4 \times 256 \times 4) = 72 + 4,096 = 4,168 \text{ bytes}$$

2. **Computational Invariance:**
   Because 521 full 16-round Feistel encryptions must execute to produce the subkeys, the computational cost of initialization is dominated by these 521 encryptions ($>99.5\%$ of operations). The 18 initial XOR operations represent $<0.5\%$ of latency, leading to the hypothesis that **cipher initialization latency is statistically independent of secret key length**.

3. **Steady-State Invariance:**
   During data encryption, the secret key is never referenced directly; all 16 Feistel rounds execute purely against the precomputed 4,168-byte subkey tables in memory. Thus, **steady-state encryption throughput is theoretically identical across all key lengths**.
