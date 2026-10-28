"""
Unit tests for Blowfish CBC and CTR encryption/decryption,
PKCS#7 padding correctness, IV randomness, and SHA-256 integrity checks.
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from blowfish_engine import (
    BlowfishCBC,
    BlowfishCTR,
    pad_pkcs7,
    unpad_pkcs7,
    generate_key,
    verify_round_trip,
    BLOCK_SIZE_BYTES,
    BENCHMARK_KEY_BITS
)


def test_pkcs7_padding_roundtrip():
    """Verify that PKCS#7 padding and unpadding round-trips correctly for various lengths."""
    for length in [0, 1, 2, 7, 8, 9, 15, 16, 17, 100, 1024]:
        data = os.urandom(length)
        padded = pad_pkcs7(data, BLOCK_SIZE_BYTES)
        assert len(padded) % BLOCK_SIZE_BYTES == 0, f"Padded length {len(padded)} not multiple of 8"
        assert len(padded) > len(data), "Padding must append at least 1 byte"
        unpadded = unpad_pkcs7(padded, BLOCK_SIZE_BYTES)
        assert unpadded == data, f"Unpadded data does not match original for length {length}"


def test_pkcs7_unpad_rejects_corrupted_padding():
    """Verify that tampered or invalid padding raises ValueError."""
    # Data length not multiple of 8
    with pytest.raises(ValueError):
        unpad_pkcs7(b"1234567")

    # Empty data
    with pytest.raises(ValueError):
        unpad_pkcs7(b"")

    # Corrupt last byte (0 is invalid PKCS7 pad byte)
    corrupted_pad_val = b"1234567\x00"
    with pytest.raises(ValueError):
        unpad_pkcs7(corrupted_pad_val)

    # Inconsistent pad bytes (says pad length 4, but only last byte is 4)
    inconsistent_pad = b"1234\x01\x02\x03\x04"
    with pytest.raises(ValueError):
        unpad_pkcs7(inconsistent_pad)


def test_cbc_round_trip_all_key_sizes():
    """Verify that every one of the 14 benchmark key sizes can successfully encrypt and decrypt."""
    test_payload = b"Reproducible Blowfish Performance Research 2026!"
    for bits in BENCHMARK_KEY_BITS:
        key = generate_key(bits)
        passed, orig_hash, dec_hash = verify_round_trip(key, test_payload)
        assert passed, f"Round trip failed for key size {bits} bits"
        assert orig_hash == dec_hash


def test_cbc_empty_and_boundary_payloads():
    """Test encryption on empty, 1-byte, 7-byte, 8-byte, and 9-byte payloads."""
    key = generate_key(128)
    engine = BlowfishCBC(key)

    payloads = [
        b"",
        b"X",
        b"1234567",
        b"12345678",
        b"123456789",
        os.urandom(1024),
        os.urandom(65536)
    ]

    for p in payloads:
        ciphertext, iv = engine.encrypt(p)
        assert len(ciphertext) % BLOCK_SIZE_BYTES == 0
        assert len(iv) == BLOCK_SIZE_BYTES
        recovered = engine.decrypt(ciphertext, iv)
        assert recovered == p, f"Decryption mismatch for payload length {len(p)}"


def test_cbc_iv_freshness():
    """Verify that encrypting identical data twice with the same key produces unique IVs and ciphertexts."""
    key = generate_key(256)
    engine = BlowfishCBC(key)
    plaintext = b"Confidential security data stream"

    c1, iv1 = engine.encrypt(plaintext)
    c2, iv2 = engine.encrypt(plaintext)

    assert iv1 != iv2, "IV was reused across consecutive encryptions!"
    assert c1 != c2, "Ciphertexts must differ when unique IVs are used!"


def test_ctr_mode_round_trip():
    """Verify CTR mode encryption and decryption."""
    key = generate_key(128)
    ctr_engine = BlowfishCTR(key)
    plaintext = b"Blowfish CTR Mode Stream Test 12345"

    ciphertext, nonce_prefix = ctr_engine.encrypt(plaintext)
    assert len(ciphertext) == len(plaintext), "CTR ciphertext length must match plaintext length exactly"
    recovered = ctr_engine.decrypt(ciphertext, nonce_prefix)
    assert recovered == plaintext
