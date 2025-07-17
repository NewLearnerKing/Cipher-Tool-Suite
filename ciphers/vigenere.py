from .base import Cipher
from . import InvalidKeyError, preserve_case

class VigenereCipher(Cipher):
    """Vigenère cipher implementation."""

    def encrypt(self, plaintext: str, key: str) -> str:
        if not key.isalpha():
            raise InvalidKeyError("Key for Vigenère cipher must be alphabetic.")
        result = ''
        key = self._format_key(plaintext, key)
        for p, k in zip(plaintext, key):
            if p.isalpha():
                base = ord('A') if p.isupper() else ord('a')
                shift = ord(k.lower()) - ord('a')
                shifted = chr((ord(p) - base + shift) % 26 + base)
                result += preserve_case(p, shifted)
            else:
                result += p
        return result

    def decrypt(self, ciphertext: str, key: str) -> str:
        if not key.isalpha():
            raise InvalidKeyError("Key for Vigenère cipher must be alphabetic.")
        result = ''
        key = self._format_key(ciphertext, key)
        for c, k in zip(ciphertext, key):
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                shift = ord(k.lower()) - ord('a')
                shifted = chr((ord(c) - base - shift) % 26 + base)
                result += preserve_case(c, shifted)
            else:
                result += c
        return result

    def _format_key(self, text: str, key: str) -> str:
        key = key.lower()
        key_sequence = ''
        key_index = 0
        for char in text:
            if char.isalpha():
                key_sequence += key[key_index % len(key)]
                key_index += 1
            else:
                key_sequence += char
        return key_sequence 