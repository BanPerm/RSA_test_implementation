"""Contain Mathematical functions for RSA.

This module provides:
- Modular inverse calculation via the extended Euclidean algorithm.
- Extended Euclidean algorithm implementation.
- RSA encryption and decryption functions.
"""

def modinv(a: int, m: int) -> int|None:
    """Modular inverse via extended Euclidean.

    Args:
      a: The integer for which the inverse is sought.
      m: Modulo

    Returns:
        The inverse of `a` modulo `m` if it exists, otherwise None.

    """
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        return None
    return x % m

def extended_gcd(a: int, b:int ) -> tuple[int,int,int]:
    """Compute the extended Euclidean algorithm.

    Args:
      a: First Integer
      b: Second Integer

    Returns:
        tuple[int, int, int]:
            - gcd(a, b): the greatest common divisor of a and b
            - x, y: coefficients such that a*x + b*y = gcd(a, b)

    """
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def rsa_chiffre(m: str, e: int, n:int) -> int:
    """Encrypt an integer message using the RSA public key.

    Args:
        m: The message to encrypt, represented as an integer.
        e: The public exponent.
        n: The modulus of the public key.

    Returns:
        The encrypted message as an integer.

    """
    a = m % n
    return pow(a, e, n)

def rsa_dechiffre(c: int, d: int, n: int) -> int:
    """Decrypt an integer message using the RSA private key.

    Args:
        c: The encrypted message to decrypt.
        d: The private exponent.
        n: The modulus of the private key.

    Returns:
        The decrypted message as an integer.

    """
    a = c % n
    return pow(a, d, n)
