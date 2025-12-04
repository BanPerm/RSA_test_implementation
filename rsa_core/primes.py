"""Handle prime number generation.

This module provides:
- Ways to generate random numbers of specified bit sizes.
- Implementation of the Sieve of Eratosthenes algorithm to find prime numbers.$
- Primality testing using trial division and the Miller-Rabin algorithm.
- Functionality to generate large prime numbers suitable for cryptographic applications.
"""

import secrets

first_prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383]  # noqa: E501

def random_bit(n: int) -> int:
    """Generate a random number of size n bits.

    Args:
        n: Number of bis

    Returns:
        Random number with n bits

    """
    return secrets.randbelow(2**n - 1 - (2**(n-1)+1)) + (2**(n-1)+1)

def sieve_eratosthene(n: int) -> list[int]:
    """Calculate list of first prime number.

    Args:
        n: Max number to test

    Returns:
        List of n first prime number

    """
    prime = [True] * (n+1)
    p=2

    while p*p <= n:
        if prime[p]:
            for i in range(p*p, n+1, p):
                prime[i] = False
        p+=1

    return [p for p in range(2,n+1) if prime[p]]

def primality_test(n: int) -> int:
    """Test if n is probably a prime number.

    Args:
        n: Number we want to test

    Returns:
        Random number with n bits

    """
    while True:
        candidate = random_bit(n)
        is_prime = True
        for p in first_prime_list:
            if p * p > candidate:
                break
            if candidate % p == 0:
                is_prime = False
                break

        if is_prime:
            return candidate

def is_miller_rabin_passed(n:int, k:int=20) -> int:
    """Test if n is probably a prime number.

    Args:
        n: Number we want tot test
        k: Number of round (more accurate if bigger)

    Returns:
        Random number with n bits

    """
    if n<2:
        return False

    if n in {2, 3}:
        return True

    if n%2 == 0:
        return False

    r = 0
    s = n-1
    while s%2 == 0:
        r+=1
        s//=2
    for _ in range(k):
        a = secrets.randbelow(n - 3) + 2
        x = pow(a,s,n)
        if x==1 or x==n-1:
            continue
        for _ in range(r-1):
            x = pow(x,2,n)
            if x==n-1:
                break
        else:
            return False
    return True


def generate_prime_number(n: int) -> int:
    """Generate a prime number with n bits.

    Args:
        n: Number of bits

    Returns:
        Prime number with n bits

    """
    while True:
        candidate = secrets.randbits(n)
        # force odd and highest bit at 1
        candidate |= (1 << (n - 1)) | 1
        if is_miller_rabin_passed(candidate):
            return candidate
