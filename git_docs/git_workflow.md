# Git Synchronization & Workflow Protocol

**Project:** `cns ise` — Blowfish Variable-Key Cryptographic Benchmarking  
**Course:** Cryptography and Network Security (CNS) A.Y. 2026–27  
**Faculty In-Charge:** Prof. Renuka Pawar  
**Institution:** Sardar Patel Institute of Technology, Mumbai  

---

## 1. Local-First Version Control Strategy
In accordance with institutional requirements, all phase outputs and final submission deliverables exist permanently on the local laptop disk. Git versioning serves as the audit trail:

1. **Phase 1 Commit:** `feat(phase-1): data lock, deterministic test payloads, and environment snapshot`
2. **Phase 2 Commit:** `feat(phase-2): blowfish engine tuning, unit tests, and isolated pilot benchmarks`
3. **Phase 3 Commit:** `feat(phase-3): tournament benchmark execution, 1820 trials, and 12 figures`
4. **Phase 4 Commit:** `feat(phase-4): overleaf manuscript compilation, presentation slides, and checklist`
5. **Final Submission Commit:** `release(final): verified deliverables package in FINAL_SUBMISSION`

---

## 2. Git Commands for Manual Sync
```powershell
# Open terminal in project root
cd "c:\Users\Rutuja Hirudkar\OneDrive\c\amazon\cns ise"

# Check status
git status

# Stage all files
git add .

# Create verified milestone commit
git commit -m "feat(cns-ise): complete 4-phase collaborative R&D deliverables and final submission"

# Add remote if connected
# git remote add origin https://github.com/Rutuja200630/cns-ise.git
# git branch -M main
# git push -u origin main
```
