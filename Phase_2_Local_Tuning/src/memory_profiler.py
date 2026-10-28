"""
Dual-layer memory profiler (tracemalloc + psutil) for Phase 2 Local Tuning.
"""

import os
import tracemalloc
from typing import Dict, Any

try:
    import psutil
    _PROCESS = psutil.Process(os.getpid())
except ImportError:
    psutil = None
    _PROCESS = None


class MemoryProfiler:
    def __init__(self):
        self.baseline_traced: int = 0
        self.peak_traced: int = 0
        self.incremental_traced: int = 0
        self.baseline_rss: int = 0
        self.peak_rss: int = 0
        self.incremental_rss: int = 0
        self._is_active: bool = False

    def start(self) -> None:
        if not tracemalloc.is_tracing():
            tracemalloc.start()
        tracemalloc.reset_peak()
        current, _ = tracemalloc.get_traced_memory()
        self.baseline_traced = current

        if _PROCESS:
            try:
                self.baseline_rss = _PROCESS.memory_info().rss
            except Exception:
                self.baseline_rss = 0
        else:
            self.baseline_rss = 0

        self._is_active = True

    def stop(self) -> Dict[str, Any]:
        if not self._is_active:
            raise RuntimeError("MemoryProfiler must be started before calling stop().")

        current, peak = tracemalloc.get_traced_memory()
        self.peak_traced = peak
        self.incremental_traced = max(0, peak - self.baseline_traced)

        if _PROCESS:
            try:
                current_rss = _PROCESS.memory_info().rss
                self.peak_rss = current_rss
                self.incremental_rss = max(0, current_rss - self.baseline_rss)
            except Exception:
                self.peak_rss = self.baseline_rss
                self.incremental_rss = 0
        else:
            self.peak_rss = 0
            self.incremental_rss = 0

        self._is_active = False
        return self.get_summary()

    def get_summary(self) -> Dict[str, Any]:
        return {
            "baseline_tracemalloc_bytes": self.baseline_traced,
            "peak_tracemalloc_bytes": self.peak_traced,
            "incremental_peak_bytes": self.incremental_traced,
            "baseline_rss_bytes": self.baseline_rss,
            "peak_rss_bytes": self.peak_rss,
            "incremental_rss_bytes": self.incremental_rss,
            "incremental_peak_kib": round(self.incremental_traced / 1024, 2),
            "peak_rss_mib": round(self.peak_rss / (1024 * 1024), 2)
        }

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
