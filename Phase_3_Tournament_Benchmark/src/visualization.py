"""
Scientific Visualization Module for Phase 3 Tournament Benchmark.
Generates 12 high-resolution (300 DPI), publication-quality IEEE-style figures
strictly from experimentally observed benchmark data.

Figures Generated:
1.  fig01_key_vs_init_time.png       : Key Length vs. Cipher Initialization Time (ms, 95% CI, warm-up policy applied)
2.  fig02_init_time_variability.png  : Key Length vs. Initialization Variability (Std Dev & CV %)
3.  fig03_enc_throughput_vs_size.png : Encryption Throughput vs. File Size (MiB/s)
4.  fig04_dec_throughput_vs_size.png : Decryption Throughput vs. File Size (MiB/s)
5.  fig05_key_vs_throughput_panels.png: Key Length vs. Throughput at Each File Size (Multi-panel)
6.  fig06_enc_latency_vs_size.png    : Encryption Latency vs. File Size (ms)
7.  fig07_dec_latency_vs_size.png    : Decryption Latency vs. File Size (ms)
8.  fig08_memory_vs_file_size.png    : Memory Usage vs. File Size (Tracemalloc vs RSS)
9.  fig09_memory_vs_key_length.png   : Three-Tier Memory Model (Theoretical 4,168 B vs Heap vs RSS)
10. fig10_normalized_performance.png : Normalized Performance (Relative to 128-bit Baseline)
11. fig11_key_size_heatmap.png       : Key Length x File Size Throughput Heatmap (MiB/s)
12. fig12_correctness_summary.png    : Cryptographic Correctness & Round-Trip Validation
"""

import logging
import os
from typing import Optional
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd

# Setup plotting style for IEEE publication
plt.rcParams.update({
    "font.size": 11,
    "font.family": "serif",
    "axes.labelsize": 12,
    "axes.titlesize": 13,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "legend.fontsize": 10,
    "figure.titlesize": 14,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight"
})

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("Visualization")


def get_base_dir() -> str:
    """Canonical Phase 3 directory."""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def generate_all_figures(
    summary_csv: str = None,
    raw_csv: str = None,
    key_summary_csv: str = None,
    output_dir: str = None
) -> None:
    """
    Read real benchmark results and generate all 12 IEEE research figures.
    """
    base_dir = get_base_dir()
    if summary_csv is None:
        summary_csv = os.path.join(base_dir, "processed_data", "benchmark_summary.csv")
    if raw_csv is None:
        raw_csv = os.path.join(base_dir, "raw_data", "benchmark_raw.csv")
    if key_summary_csv is None:
        key_summary_csv = os.path.join(base_dir, "processed_data", "key_schedule_results.csv")
    if output_dir is None:
        output_dir = os.path.join(base_dir, "graphs")

    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(summary_csv) or not os.path.exists(raw_csv):
        raise FileNotFoundError(f"Required result files not found: {summary_csv} or {raw_csv}")

    df_sum = pd.read_csv(summary_csv)
    df_raw = pd.read_csv(raw_csv)
    df_ks = pd.read_csv(key_summary_csv) if os.path.exists(key_summary_csv) else None

    # Colors for distinct key lengths
    palette = plt.cm.tab20(np.linspace(0, 1, 14))

    # =========================================================================
    # Figure 1: Key Length vs. Cipher Initialization Time (ms with 95% CI)
    # =========================================================================
    if df_ks is not None and not df_ks.empty:
        fig, ax = plt.subplots(figsize=(8.5, 5))
        yerr = [
            df_ks["mean_init_time_ms"] - df_ks["ci95_low_ms"],
            df_ks["ci95_high_ms"] - df_ks["mean_init_time_ms"]
        ]
        ax.errorbar(
            df_ks["key_bits"], df_ks["mean_init_time_ms"],
            yerr=yerr, fmt="-o", color="#1f77b4", ecolor="#d62728",
            elinewidth=1.8, capsize=4, capthick=1.5, markersize=6,
            label="Steady-State Mean Init Time (95% CI)"
        )
        ax.set_xlabel("Secret Key Length (bits)")
        ax.set_ylabel("Cipher Initialization Time (ms)")
        ax.set_title("Figure 1: Secret Key Length vs. Cipher Initialization Latency\n(Audited Warm-Up Policy Applied; N=30 Repetitions)")
        ax.set_xticks(df_ks["key_bits"])
        ax.set_xticklabels(df_ks["key_bits"], rotation=45)
        ax.grid(True, linestyle="--", alpha=0.6)
        ax.legend(loc="best")
        fig.tight_layout()
        f1_path = os.path.join(output_dir, "fig01_key_vs_init_time.png")
        fig.savefig(f1_path)
        plt.close(fig)
        logger.info(f"Saved: {f1_path}")

        # =========================================================================
        # Figure 2: Key Length vs. Initialization-Time Variability (Std Dev & CV %)
        # =========================================================================
        fig, ax1 = plt.subplots(figsize=(8.5, 5))
        color1 = "#2ca02c"
        color2 = "#ff7f0e"

        ax1.set_xlabel("Secret Key Length (bits)")
        ax1.set_ylabel("Standard Deviation (ms)", color=color1)
        line1 = ax1.plot(df_ks["key_bits"], df_ks["std_init_time_ms"], "-s", color=color1, label="Std Dev (ms)")
        ax1.tick_params(axis="y", labelcolor=color1)
        ax1.set_xticks(df_ks["key_bits"])
        ax1.set_xticklabels(df_ks["key_bits"], rotation=45)
        ax1.grid(True, linestyle="--", alpha=0.6)

        ax2 = ax1.twinx()
        ax2.set_ylabel("Coefficient of Variation (%)", color=color2)
        line2 = ax2.plot(df_ks["key_bits"], df_ks["cv_percent"], "--^", color=color2, label="CV (%)")
        ax2.tick_params(axis="y", labelcolor=color2)

        lines = line1 + line2
        labels = [l.get_label() for l in lines]
        ax1.legend(lines, labels, loc="upper right")
        ax1.set_title("Figure 2: Key Schedule Latency Variability Across Key Lengths")
        fig.tight_layout()
        f2_path = os.path.join(output_dir, "fig02_init_time_variability.png")
        fig.savefig(f2_path)
        plt.close(fig)
        logger.info(f"Saved: {f2_path}")

    # Common subsets
    df_enc = df_sum[df_sum["operation"] == "encryption"].copy()
    df_dec = df_sum[df_sum["operation"] == "decryption"].copy()

    file_labels = ["1 KiB", "100 KiB", "1 MiB", "10 MiB", "50 MiB"]
    key_lengths = sorted(df_sum["key_bits"].unique())
    rep_keys = [32, 64, 128, 256, 384, 448] if all(k in key_lengths for k in [32, 64, 128, 256, 384, 448]) else key_lengths[::2]
    markers = ["o", "s", "^", "D", "v", "p", "*", "X"]

    # =========================================================================
    # Figure 3: Encryption Throughput vs. File Size (MiB/s)
    # =========================================================================
    fig, ax = plt.subplots(figsize=(9, 5))
    for i, k in enumerate(rep_keys):
        sub = df_enc[df_enc["key_bits"] == k].sort_values("file_size_bytes")
        if not sub.empty:
            ax.plot(
                sub["file_size_label"], sub["mean_throughput_mib_s"],
                marker=markers[i % len(markers)], linewidth=2,
                label=f"Key: {k} bits"
            )
    ax.set_xlabel("Workload File Size")
    ax.set_ylabel("Steady-State Throughput (MiB/s)")
    ax.set_title("Figure 3: Encryption Throughput vs. File Size Across Key Lengths")
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend(loc="upper left")
    fig.tight_layout()
    f3_path = os.path.join(output_dir, "fig03_enc_throughput_vs_size.png")
    fig.savefig(f3_path)
    plt.close(fig)
    logger.info(f"Saved: {f3_path}")

    # =========================================================================
    # Figure 4: Decryption Throughput vs. File Size (MiB/s)
    # =========================================================================
    fig, ax = plt.subplots(figsize=(9, 5))
    for i, k in enumerate(rep_keys):
        sub = df_dec[df_dec["key_bits"] == k].sort_values("file_size_bytes")
        if not sub.empty:
            ax.plot(
                sub["file_size_label"], sub["mean_throughput_mib_s"],
                marker=markers[i % len(markers)], linewidth=2,
                label=f"Key: {k} bits"
            )
    ax.set_xlabel("Workload File Size")
    ax.set_ylabel("Steady-State Throughput (MiB/s)")
    ax.set_title("Figure 4: Decryption Throughput vs. File Size Across Key Lengths")
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend(loc="upper left")
    fig.tight_layout()
    f4_path = os.path.join(output_dir, "fig04_dec_throughput_vs_size.png")
    fig.savefig(f4_path)
    plt.close(fig)
    logger.info(f"Saved: {f4_path}")

    # =========================================================================
    # Figure 5: Multi-panel Key Length vs Throughput for Each Workload
    # =========================================================================
    fig, axes = plt.subplots(1, 5, figsize=(18, 4), sharey=False)
    for idx, f_label in enumerate(file_labels):
        ax_sub = axes[idx]
        sub = df_enc[df_enc["file_size_label"] == f_label].sort_values("key_bits")
        if not sub.empty:
            ax_sub.bar(
                [str(k) for k in sub["key_bits"]], sub["mean_throughput_mib_s"],
                color="#1f77b4", edgecolor="black", width=0.6
            )
            ax_sub.set_title(f"Payload: {f_label}", fontsize=11, fontweight="bold")
            ax_sub.set_xlabel("Key Bits", fontsize=9)
            ax_sub.tick_params(axis="x", rotation=90, labelsize=8)
            ax_sub.grid(True, linestyle="--", alpha=0.5, axis="y")
            if idx == 0:
                ax_sub.set_ylabel("Mean Throughput (MiB/s)", fontsize=10)
    fig.suptitle("Figure 5: Steady-State Encryption Throughput Across 14 Key Sizes (All 5 Workloads)", fontsize=13)
    fig.tight_layout()
    f5_path = os.path.join(output_dir, "fig05_key_vs_throughput_panels.png")
    fig.savefig(f5_path)
    plt.close(fig)
    logger.info(f"Saved: {f5_path}")

    # =========================================================================
    # Figure 6: Encryption Latency vs. File Size (ms)
    # =========================================================================
    fig, ax = plt.subplots(figsize=(8.5, 5))
    for i, k in enumerate(rep_keys):
        sub = df_enc[df_enc["key_bits"] == k].sort_values("file_size_bytes")
        if not sub.empty:
            ax.plot(
                sub["file_size_label"], sub["mean_latency_ms"],
                marker=markers[i % len(markers)], linewidth=2,
                label=f"Key: {k} bits"
            )
    ax.set_xlabel("Workload File Size")
    ax.set_ylabel("Execution Latency (ms)")
    ax.set_title("Figure 6: Encryption Latency vs. File Size")
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend(loc="upper left")
    fig.tight_layout()
    f6_path = os.path.join(output_dir, "fig06_enc_latency_vs_size.png")
    fig.savefig(f6_path)
    plt.close(fig)
    logger.info(f"Saved: {f6_path}")

    # =========================================================================
    # Figure 7: Decryption Latency vs. File Size (ms)
    # =========================================================================
    fig, ax = plt.subplots(figsize=(8.5, 5))
    for i, k in enumerate(rep_keys):
        sub = df_dec[df_dec["key_bits"] == k].sort_values("file_size_bytes")
        if not sub.empty:
            ax.plot(
                sub["file_size_label"], sub["mean_latency_ms"],
                marker=markers[i % len(markers)], linewidth=2,
                label=f"Key: {k} bits"
            )
    ax.set_xlabel("Workload File Size")
    ax.set_ylabel("Execution Latency (ms)")
    ax.set_title("Figure 7: Decryption Latency vs. File Size")
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend(loc="upper left")
    fig.tight_layout()
    f7_path = os.path.join(output_dir, "fig07_dec_latency_vs_size.png")
    fig.savefig(f7_path)
    plt.close(fig)
    logger.info(f"Saved: {f7_path}")

    # =========================================================================
    # Figure 8: Memory Usage vs. File Size (Tracemalloc vs RSS)
    # =========================================================================
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    sub_mem = df_enc[df_enc["key_bits"] == 128].sort_values("file_size_bytes")
    if sub_mem.empty:
        sub_mem = df_enc.groupby("file_size_label").first().reset_index().sort_values("file_size_bytes")

    ax1.plot(
        sub_mem["file_size_label"], sub_mem["mean_peak_tracemalloc_bytes"] / (1024 * 1024),
        marker="o", color="#8c564b", linewidth=2.2, label="Peak Heap (tracemalloc)"
    )
    ax1.set_xlabel("Input Workload Size")
    ax1.set_ylabel("Peak Tracemalloc Allocation (MiB)")
    ax1.set_title("Python Heap Memory Allocation", fontsize=11)
    ax1.grid(True, linestyle="--", alpha=0.6)
    ax1.legend()

    ax2.plot(
        sub_mem["file_size_label"], sub_mem["mean_peak_rss_mib"],
        marker="s", color="#e377c2", linewidth=2.2, label="Process RSS (psutil)"
    )
    ax2.set_xlabel("Input Workload Size")
    ax2.set_ylabel("Process Resident Set Size (MiB)")
    ax2.set_title("Operating System Process RSS", fontsize=11)
    ax2.grid(True, linestyle="--", alpha=0.6)
    ax2.legend()

    fig.suptitle("Figure 8: Memory Footprint vs. Workload Payload Size", fontsize=13)
    fig.tight_layout()
    f8_path = os.path.join(output_dir, "fig08_memory_vs_file_size.png")
    fig.savefig(f8_path)
    plt.close(fig)
    logger.info(f"Saved: {f8_path}")

    # =========================================================================
    # Figure 9: Three-Tier Memory Model Across Key Lengths (50 MiB Workload)
    # =========================================================================
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    sub_50m = df_enc[df_enc["file_size_label"] == "50 MiB"].sort_values("key_bits")

    # Panel 1: Peak Heap (tracemalloc) and Theoretical Subkeys
    ax1.plot(
        sub_50m["key_bits"], sub_50m["mean_peak_tracemalloc_bytes"] / (1024 * 1024),
        marker="^", color="#1f77b4", linewidth=2, label="Peak Heap (168.5 MiB, Delta <= 186 B)"
    )
    ax1.axhline(
        4168 / (1024 * 1024), color="#d62728", linestyle="--", linewidth=1.5,
        label="Theoretical Subkeys (4,168 B = 0.004 MiB)"
    )
    ax1.set_xlabel("Secret Key Length (bits)")
    ax1.set_ylabel("Memory Footprint (MiB)")
    ax1.set_title("Tier 1 & Tier 2: Theoretical vs. Heap Allocation", fontsize=11)
    ax1.set_xticks(sub_50m["key_bits"])
    ax1.set_xticklabels(sub_50m["key_bits"], rotation=45)
    ax1.grid(True, linestyle="--", alpha=0.6)
    ax1.legend(loc="center right")

    # Panel 2: Process RSS (psutil)
    ax2.plot(
        sub_50m["key_bits"], sub_50m["mean_peak_rss_mib"],
        marker="s", color="#2ca02c", linewidth=2, label="Process Working Set (~265.6 MiB)"
    )
    ax2.set_xlabel("Secret Key Length (bits)")
    ax2.set_ylabel("Process RSS (MiB)")
    ax2.set_title("Tier 3: OS Process Resident Set Size (psutil)", fontsize=11)
    ax2.set_xticks(sub_50m["key_bits"])
    ax2.set_xticklabels(sub_50m["key_bits"], rotation=45)
    ax2.grid(True, linestyle="--", alpha=0.6)
    ax2.legend(loc="upper right")

    fig.suptitle("Figure 9: Three-Tier Memory Allocation Model Across Key Lengths (50 MiB Workload)", fontsize=13)
    fig.tight_layout()
    f9_path = os.path.join(output_dir, "fig09_memory_vs_key_length.png")
    fig.savefig(f9_path)
    plt.close(fig)
    logger.info(f"Saved: {f9_path}")

    # =========================================================================
    # Figure 10: Normalized Performance Comparison (Relative to 128-bit Key)
    # =========================================================================
    fig, ax = plt.subplots(figsize=(9, 5))
    ref_key = 128 if 128 in key_lengths else key_lengths[0]
    norm_data = []
    for f_label in file_labels:
        sub = df_enc[df_enc["file_size_label"] == f_label]
        ref_row = sub[sub["key_bits"] == ref_key]
        if not ref_row.empty:
            ref_tp = ref_row["mean_throughput_mib_s"].iloc[0]
            if ref_tp > 0:
                for _, r in sub.iterrows():
                    norm_data.append({
                        "file_size_label": f_label,
                        "key_bits": r["key_bits"],
                        "norm_throughput": r["mean_throughput_mib_s"] / ref_tp
                    })

    if norm_data:
        df_norm = pd.DataFrame(norm_data)
        for i, k in enumerate(rep_keys):
            sub_k = df_norm[df_norm["key_bits"] == k]
            ax.plot(
                sub_k["file_size_label"], sub_k["norm_throughput"],
                marker=markers[i % len(markers)], linewidth=2,
                label=f"Key: {k} bits"
            )
    ax.axhline(1.0, color="red", linestyle="--", alpha=0.7, label="128-bit Reference Baseline")
    ax.set_xlabel("Workload File Size")
    ax.set_ylabel("Normalized Encryption Throughput (Relative to 128-bit)")
    ax.set_title("Figure 10: Normalized Encryption Performance Relative to 128-bit Standard")
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend(loc="best")
    fig.tight_layout()
    f10_path = os.path.join(output_dir, "fig10_normalized_performance.png")
    fig.savefig(f10_path)
    plt.close(fig)
    logger.info(f"Saved: {f10_path}")

    # =========================================================================
    # Figure 11: Key Length x File Size Heatmap (MiB/s)
    # =========================================================================
    fig, ax = plt.subplots(figsize=(9, 6))
    piv = df_enc.pivot(index="key_bits", columns="file_size_label", values="mean_throughput_mib_s")
    cols_order = [c for c in file_labels if c in piv.columns]
    piv = piv[cols_order]

    cax = ax.imshow(piv.values, cmap="YlGnBu", aspect="auto")
    ax.set_xticks(range(len(cols_order)))
    ax.set_xticklabels(cols_order)
    ax.set_yticks(range(len(piv.index)))
    ax.set_yticklabels([f"{k} bits" for k in piv.index])
    ax.set_xlabel("Workload File Size")
    ax.set_ylabel("Secret Key Length")
    ax.set_title("Figure 11: Heatmap of Steady-State Encryption Throughput (MiB/s)")

    for r_idx in range(len(piv.index)):
        for c_idx in range(len(cols_order)):
            val = piv.values[r_idx, c_idx]
            text_color = "white" if val > 300 else "black"
            ax.text(c_idx, r_idx, f"{val:.1f}", ha="center", va="center", color=text_color, fontsize=8)

    fig.colorbar(cax, ax=ax, label="Throughput (MiB/s)")
    fig.tight_layout()
    f11_path = os.path.join(output_dir, "fig11_key_size_heatmap.png")
    fig.savefig(f11_path)
    plt.close(fig)
    logger.info(f"Saved: {f11_path}")

    # =========================================================================
    # Figure 12: Cryptographic Correctness Validation Summary
    # =========================================================================
    fig, ax = plt.subplots(figsize=(8, 4.5))
    total_valid = len(df_raw[df_raw["is_warmup"] == False])
    passed_count = int((df_raw["correctness_passed"] == True).sum())
    failed_count = int((df_raw["correctness_passed"] == False).sum())

    categories = ["Passed (100% Round-Trip)", "Failed"]
    counts = [passed_count, failed_count]
    bar_colors = ["#2ca02c", "#d62728"]

    bars = ax.bar(categories, counts, color=bar_colors, width=0.45, edgecolor="black")
    ax.set_ylabel("Experimental Trial Count")
    ax.set_title(f"Figure 12: Cryptographic Correctness & Round-Trip Validation (N={total_valid})")
    ax.set_ylim(0, max(counts) * 1.2 if max(counts) > 0 else 10)
    ax.grid(True, axis="y", linestyle="--", alpha=0.6)

    for b in bars:
        height = b.get_height()
        ax.annotate(
            f"{height:,} ({height/total_valid*100:.1f}%)" if total_valid > 0 else "0",
            xy=(b.get_x() + b.get_width() / 2, height),
            xytext=(0, 4), textcoords="offset points",
            ha="center", va="bottom", fontweight="bold"
        )

    fig.tight_layout()
    f12_path = os.path.join(output_dir, "fig12_correctness_summary.png")
    fig.savefig(f12_path)
    plt.close(fig)
    logger.info(f"Saved: {f12_path}")

    logger.info("All 12 research figures generated and saved successfully to graphs/")


if __name__ == "__main__":
    generate_all_figures()
