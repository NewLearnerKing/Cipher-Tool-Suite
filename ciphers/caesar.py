from .base import Cipher
from . import InvalidKeyError, preserve_case

class CaesarCipher(Cipher):
    """Caesar cipher implementation."""

    def encrypt(self, plaintext: str, key: str) -> str:
        try:
            shift = int(key) % 26
        except ValueError:
            raise InvalidKeyError("Key for Caesar cipher must be an integer.")
        result = ''
        for char in plaintext:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = chr((ord(char) - base + shift) % 26 + base)
                result += preserve_case(char, shifted)
            else:
                result += char
        return result

    def decrypt(self, ciphertext: str, key: str) -> str:
        try:
            shift = int(key) % 26
        except ValueError:
            raise InvalidKeyError("Key for Caesar cipher must be an integer.")
        result = ''
        for char in ciphertext:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = chr((ord(char) - base - shift) % 26 + base)
                result += preserve_case(char, shifted)
            else:
                result += char
        return result 