"""
Unit tests for Blowfish key generation and key-length validation.
Verifies compliance across all 14 benchmark key sizes (32 to 448 bits)
and rejection of boundary and invalid key lengths.
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from blowfish_engine import (
    validate_key_length,
    generate_key,
    BENCHMARK_KEY_BITS,
    MIN_KEY_BYTES,
    MAX_KEY_BYTES
)


def test_valid_benchmark_key_lengths():
    """Verify that all 14 benchmark key sizes generate exact byte lengths and pass validation."""
    for bits in BENCHMARK_KEY_BITS:
        key = generate_key(bits)
        expected_bytes = bits // 8
        assert len(key) == expected_bytes, f"Expected {expected_bytes} bytes for {bits} bits, got {len(key)}"
        # Must not raise
        validate_key_length(key)


def test_key_length_boundaries():
    """Verify lower boundary (4 bytes / 32 bits) and upper boundary (56 bytes / 448 bits)."""
    # Min valid
    min_key = b"A" * MIN_KEY_BYTES
    validate_key_length(min_key)

    # Max valid
    max_key = b"B" * MAX_KEY_BYTES
    validate_key_length(max_key)


def test_reject_underlength_keys():
    """Verify that keys shorter than 4 bytes (32 bits) raise ValueError."""
    for invalid_len in [0, 1, 2, 3]:
        short_key = b"\x00" * invalid_len
        with pytest.raises(ValueError):
            validate_key_length(short_key)


def test_reject_overlength_keys():
    """Verify that keys longer than 56 bytes (448 bits) raise ValueError."""
    for invalid_len in [57, 58, 64, 128]:
        long_key = b"\x00" * invalid_len
        with pytest.raises(ValueError):
            validate_key_length(long_key)


def test_reject_invalid_key_types():
    """Verify non-bytes keys raise TypeError."""
    for invalid in ["secret_string", 12345, [1, 2, 3, 4], None]:
        with pytest.raises(TypeError):
            validate_key_length(invalid)


def test_generate_key_rejects_non_multiple_of_8():
    """Verify key generation rejects non-byte-aligned bit lengths."""
    for invalid_bits in [33, 45, 100, 447]:
        with pytest.raises(ValueError):
            generate_key(invalid_bits)
