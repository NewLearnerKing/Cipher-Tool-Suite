from .base import Cipher
from . import InvalidKeyError
import string

class SubstitutionCipher(Cipher):
    """Monoalphabetic substitution cipher implementation."""

    def _validate_key(self, key: str):
        key = key.upper()
        if len(key) != 26 or not all(c.isalpha() for c in key):
            raise InvalidKeyError("Key for Substitution cipher must be 26 unique alphabetic characters.")
        if len(set(key)) != 26:
            raise InvalidKeyError("Key for Substitution cipher must not contain repeated letters.")
        return key

    def encrypt(self, plaintext: str, key: str) -> str:
        key = self._validate_key(key)
        table = {c: k for c, k in zip(string.ascii_uppercase, key)}
        result = ''
        for char in plaintext:
            if char.isalpha():
                upper = char.upper()
                sub = table[upper]
                result += sub if char.isupper() else sub.lower()
            else:
                result += char
        return result

    def decrypt(self, ciphertext: str, key: str) -> str:
        key = self._validate_key(key)
        table = {k: c for c, k in zip(string.ascii_uppercase, key)}
        result = ''
        for char in ciphertext:
            if char.isalpha():
                upper = char.upper()
                sub = table[upper]
                result += sub if char.isupper() else sub.lower()
            else:
                result += char
        return result 