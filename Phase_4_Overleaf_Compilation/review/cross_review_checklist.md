# Phase 4: Overleaf Compilation & Cross-Review Checklist

**Course:** Cryptography and Network Security (CNS) A.Y. 2026–27  
**Faculty In-Charge:** Prof. Renuka Pawar  
**Institution:** Sardar Patel Institute of Technology, Mumbai  
**Milestone:** End of Week 4 (Overleaf Compilation & Cross-Review)  

---

## 1. Collaborative Overleaf Compilation Criteria

- [x] **Master Template Compliance:** Follows standard two-column `IEEEtran` conference/journal document class (`\documentclass[conference]{IEEEtran}`).
- [x] **Mathematical Equations Transcribed:**
  - Feistel round equations: $L_i = R_{i-1} \oplus P_i$ and $R_i = L_{i-1} \oplus F(L_i)$.
  - $F$-function arithmetic: $F(x) = ((S_1[a] + S_2[b] \bmod 2^{32}) \oplus S_3[c]) + S_4[d] \bmod 2^{32}$.
  - Subkey generation cycle: Exactly 521 iterative block encryptions.
  - Sweet32 birthday bound: $N \approx 2^{32}\text{ blocks} = 32\text{ GiB}$.
- [x] **Cross-References Integrity:**
  - All figures cited in text via `\ref{fig:...}`.
  - All tables cited in text via `\ref{tab:...}`.
  - All bibliography entries cited in text via `\cite{...}`.
- [x] **Authentic Bibliography (`references.bib`):**
  - Schneier 1993 (FSE / LNCS 809).
  - NIST SP 800-38A (Dworkin 2001).
  - Bhargavan & Leurent Sweet32 (ACM CCS 2016).
  - Kelsey, Schneier, Wagner, Hall (CRYPTO '96).
  - Biham related-key attacks (Journal of Cryptology 1994).
  - Ferguson, Schneier, Kohno (Wiley 2010).
  - PyCryptodome official documentation.
  - **Zero fabricated citations.**
- [x] **Turnitin Plagiarism Target (<15%):**
  - All technical descriptions of methodology, experimental setup, and results are original academic prose.
  - Mathematical equations and standard standard names (NIST SP 800-38A) properly quoted and cited.
  - Anticipated similarity score: **< 10%** (well within the institutional 15% threshold).
- [x] **Multi-Author Sign-off:**
  - Student Researcher: Rutuja Hirudkar & CNS Group.
  - Faculty In-Charge: Prof. Renuka Pawar.
  - Affiliation: Sardar Patel Institute of Technology, Mumbai.
