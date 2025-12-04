"""Generation of RSA keys.

This module provides:
- Way to generate public ans private key using RSA algorithm.
"""

import math

from rsa_core.primes import generate_prime_number
from rsa_core.rsa_math import modinv


def generate_keys(size:int=1024) -> tuple[int,int,int]:
    """Generate public and private key using RSA.

    Args:
      size: number of bits use to generate random number

    Returns:
        tuple[int, int, int]: A tuple containing the RSA key components
            - e: The public exponent
            - d: The private exponent
            - n: The modulo for both public and private keys

    """
    while True:
        p = generate_prime_number(size)
        q = generate_prime_number(size)

        n = p*q
        phi = (p-1)*(q-1)

        e = 65537
        if math.gcd(e, phi) != 1:
            continue

        d = modinv(e, phi)
        if d is None:
            continue

        return e,d,n
