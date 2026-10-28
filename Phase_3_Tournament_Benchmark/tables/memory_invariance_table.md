# Three-Tier Memory Allocation Model (50 MiB Workload)

- **Tier 1 (Theoretical Subkey State):** Fixed at 4,168 B (18 P-array words + 1,024 S-box words).
- **Tier 2 (Python Heap tracemalloc):** Buffers and object management; strictly invariant to key length (variation <= 186 B).
- **Tier 3 (OS Process RSS psutil):** Whole-process working set in physical RAM.

|   key_bits |   theoretical_subkey_bytes |   mean_peak_tracemalloc_bytes |   mean_incremental_tracemalloc_bytes |   mean_peak_rss_mib |
|-----------:|---------------------------:|------------------------------:|-------------------------------------:|--------------------:|
|         32 |                       4168 |                   1.76711e+08 |                          2.94478e+07 |             265.688 |
|         64 |                       4168 |                   1.76711e+08 |                          2.94478e+07 |             265.675 |
|         96 |                       4168 |                   1.76711e+08 |                          2.94478e+07 |             265.625 |
|        128 |                       4168 |                   1.76711e+08 |                          2.94478e+07 |             265.625 |
|        160 |                       4168 |                   1.76711e+08 |                          2.94478e+07 |             265.625 |
|        192 |                       4168 |                   1.76711e+08 |                          2.94478e+07 |             265.625 |
|        224 |                       4168 |                   1.76711e+08 |                          2.94478e+07 |             265.625 |
|        256 |                       4168 |                   1.76711e+08 |                          2.94478e+07 |             265.625 |
|        288 |                       4168 |                   1.76711e+08 |                          2.94478e+07 |             265.625 |
|        320 |                       4168 |                   1.76711e+08 |                          2.94478e+07 |             265.625 |
|        352 |                       4168 |                   1.76711e+08 |                          2.94478e+07 |             265.625 |
|        384 |                       4168 |                   1.76711e+08 |                          2.94478e+07 |             265.62  |
|        416 |                       4168 |                   1.76711e+08 |                          2.94478e+07 |             265.609 |
|        448 |                       4168 |                   1.76711e+08 |                          2.94478e+07 |             265.609 |
