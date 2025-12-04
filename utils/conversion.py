"""Module for converting text messages to and from RSA-encrypted format.

This module provides:
- Functions to encrypt and decrypt text messages using RSA.
- Utility functions to convert between strings and lists of Unicode code points.
"""

from rsa_core.rsa_math import rsa_chiffre, rsa_dechiffre


def chiffre_text_rsa(m: str, e: int, n: int) -> list[str]:
    """Encrypt a text message using RSA, character by character.

    Args:
        m: The message to encrypt.
        e: The RSA public exponent.
        n: The RSA modulus.

    Returns:
        A list of encrypted numbers as strings, one for each character.

    """
    nombre = mot_to_number(m)
    return [str(rsa_chiffre(p, e, n)) for p in nombre]

def dechiffre_text_rsa(m: str, d: int, n: int) -> str:
    """Decrypt a text message previously encrypted with RSA.

    Args:
        m: The encrypted message, with numbers separated by spaces.
        d: The RSA private exponent.
        n: The RSA modulus.

    Returns:
        str: The decrypted text message.

    """
    m = m.split()
    return number_to_mot([rsa_dechiffre(int(p), d, n) for p in m])

def mot_to_number(m: str) -> list[int]:
    """Convert a string into a list of Unicode code points.

    Args:
        m: The input string.

    Returns:
        A list of integers representing the Unicode code of each character.

    """
    return [ord(x) for x in m]

def number_to_mot(m: list[int]) -> str:
    """Convert a list of Unicode code points back into a string.

    Args:
        m: A list of integers representing Unicode codes.

    Returns:
        str: The reconstructed string.

    """
    return "".join(chr(x) for x in m)
