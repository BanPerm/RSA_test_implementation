"""Initialize the RSA package.

This package provides core functionalities for RSA encryption and decryption,
including prime number generation, key generation, and mathematical operations
necessary for RSA.
"""
from rsa_core.keygen import generate_keys
from rsa_core.primes import (
    generate_prime_number,
    is_miller_rabin_passed,
    primality_test,
    random_bit,
)
from rsa_core.rsa_math import modinv, rsa_chiffre, rsa_dechiffre

__all__ = [
    "generate_keys",
    "generate_prime_number",
    "is_miller_rabin_passed",
    "modinv",
    "primality_test",
    "random_bit",
    "rsa_chiffre",
    "rsa_dechiffre",
]
