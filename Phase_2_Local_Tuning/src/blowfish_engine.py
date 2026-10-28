"""
Blowfish Cryptographic Engine Module (Phase 2 Local Tuning).
Implements the core Blowfish encryption/decryption engine using PyCryptodome.
Supports variable-length secret keys from 32 to 448 bits (4 to 56 bytes),
CBC mode with PKCS#7 padding and fresh random 64-bit IVs,
optional CTR mode, and SHA-256 payload integrity validation.
"""

import hashlib
import secrets
from typing import Tuple, Optional
from Crypto.Cipher import Blowfish
from Crypto.Util import Counter

BLOCK_SIZE_BYTES = 8  # 64 bits
MIN_KEY_BYTES = 4     # 32 bits
MAX_KEY_BYTES = 56    # 448 bits

BENCHMARK_KEY_BITS = [32, 64, 96, 128, 160, 192, 224, 256, 288, 320, 352, 384, 416, 448]


def validate_key_length(key: bytes) -> None:
    """Validate that key byte length conforms to Blowfish specifications (4 to 56 bytes)."""
    if not isinstance(key, (bytes, bytearray)):
        raise TypeError(f"Key must be bytes or bytearray, got {type(key).__name__}")
    key_len = len(key)
    if key_len < MIN_KEY_BYTES or key_len > MAX_KEY_BYTES:
        raise ValueError(
            f"Invalid key length: {key_len} bytes ({key_len * 8} bits). "
            f"Blowfish requires between {MIN_KEY_BYTES} and {MAX_KEY_BYTES} bytes (32 to 448 bits)."
        )


def generate_key(key_bits: int) -> bytes:
    """Generate a cryptographically secure random key of exactly key_bits length."""
    if key_bits % 8 != 0:
        raise ValueError(f"Key bits must be a multiple of 8, got {key_bits}")
    key_bytes = key_bits // 8
    if key_bytes < MIN_KEY_BYTES or key_bytes > MAX_KEY_BYTES:
        raise ValueError(
            f"Key bits {key_bits} ({key_bytes} bytes) out of Blowfish range (32-448 bits)."
        )
    return secrets.token_bytes(key_bytes)


def pad_pkcs7(data: bytes, block_size: int = BLOCK_SIZE_BYTES) -> bytes:
    """Apply PKCS#7 padding to data for the given block size."""
    pad_len = block_size - (len(data) % block_size)
    padding = bytes([pad_len] * pad_len)
    return data + padding


def unpad_pkcs7(padded_data: bytes, block_size: int = BLOCK_SIZE_BYTES) -> bytes:
    """Validate and remove PKCS#7 padding."""
    if not padded_data:
        raise ValueError("Cannot unpad empty bytes.")
    if len(padded_data) % block_size != 0:
        raise ValueError(f"Padded data length ({len(padded_data)}) is not a multiple of block size ({block_size}).")
    
    pad_len = padded_data[-1]
    if pad_len < 1 or pad_len > block_size:
        raise ValueError(f"Invalid PKCS#7 padding byte value: {pad_len}")
    
    expected_padding = bytes([pad_len] * pad_len)
    if padded_data[-pad_len:] != expected_padding:
        raise ValueError("Malformed PKCS#7 padding: padding bytes do not match pad length.")
    
    return padded_data[:-pad_len]


def compute_sha256(data: bytes) -> str:
    """Compute the SHA-256 hexadecimal digest of input bytes."""
    return hashlib.sha256(data).hexdigest()


class BlowfishCBC:
    """Blowfish engine in CBC mode enforcing fresh random IV and PKCS#7 padding."""

    def __init__(self, key: bytes):
        validate_key_length(key)
        self.key = key
        self.key_bytes = len(key)
        self.key_bits = self.key_bytes * 8

    def encrypt(self, plaintext: bytes, iv: Optional[bytes] = None) -> Tuple[bytes, bytes]:
        if iv is None:
            iv = secrets.token_bytes(BLOCK_SIZE_BYTES)
        elif len(iv) != BLOCK_SIZE_BYTES:
            raise ValueError(f"IV must be exactly {BLOCK_SIZE_BYTES} bytes, got {len(iv)}")

        cipher = Blowfish.new(self.key, Blowfish.MODE_CBC, iv=iv)
        padded = pad_pkcs7(plaintext, BLOCK_SIZE_BYTES)
        ciphertext = cipher.encrypt(padded)
        return ciphertext, iv

    def decrypt(self, ciphertext: bytes, iv: bytes) -> bytes:
        if len(iv) != BLOCK_SIZE_BYTES:
            raise ValueError(f"IV must be exactly {BLOCK_SIZE_BYTES} bytes, got {len(iv)}")
        if len(ciphertext) % BLOCK_SIZE_BYTES != 0:
            raise ValueError(f"Ciphertext length ({len(ciphertext)}) is not block-aligned ({BLOCK_SIZE_BYTES}).")

        cipher = Blowfish.new(self.key, Blowfish.MODE_CBC, iv=iv)
        padded = cipher.decrypt(ciphertext)
        return unpad_pkcs7(padded, BLOCK_SIZE_BYTES)

    def encrypt_raw_aligned(self, pre_padded: bytes, iv: bytes) -> bytes:
        cipher = Blowfish.new(self.key, Blowfish.MODE_CBC, iv=iv)
        return cipher.encrypt(pre_padded)

    def decrypt_raw_aligned(self, ciphertext: bytes, iv: bytes) -> bytes:
        cipher = Blowfish.new(self.key, Blowfish.MODE_CBC, iv=iv)
        return cipher.decrypt(ciphertext)


class BlowfishCTR:
    """Blowfish engine operating in Counter (CTR) mode."""

    def __init__(self, key: bytes):
        validate_key_length(key)
        self.key = key
        self.key_bytes = len(key)
        self.key_bits = self.key_bytes * 8

    def encrypt(self, plaintext: bytes, initial_counter_val: int = 1) -> Tuple[bytes, bytes]:
        prefix = secrets.token_bytes(4)
        ctr = Counter.new(32, prefix=prefix, initial_value=initial_counter_val)
        cipher = Blowfish.new(self.key, Blowfish.MODE_CTR, counter=ctr)
        ciphertext = cipher.encrypt(plaintext)
        return ciphertext, prefix

    def decrypt(self, ciphertext: bytes, prefix: bytes, initial_counter_val: int = 1) -> bytes:
        ctr = Counter.new(32, prefix=prefix, initial_value=initial_counter_val)
        cipher = Blowfish.new(self.key, Blowfish.MODE_CTR, counter=ctr)
        return cipher.decrypt(ciphertext)


def verify_round_trip(key: bytes, plaintext: bytes) -> Tuple[bool, str, str]:
    orig_hash = compute_sha256(plaintext)
    engine = BlowfishCBC(key)
    ciphertext, iv = engine.encrypt(plaintext)
    recovered = engine.decrypt(ciphertext, iv)
    dec_hash = compute_sha256(recovered)
    passed = (recovered == plaintext) and (orig_hash == dec_hash)
    return passed, orig_hash, dec_hash
