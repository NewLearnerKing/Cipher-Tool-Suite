from .base import Cipher
from . import InvalidKeyError
import string
import numpy as np
import math

class HillCipher(Cipher):
    """Hill cipher implementation (nxn matrix, n >= 2)."""

    def _key_to_matrix(self, key: str):
        """
        Convert a key string to an n x n matrix for the Hill cipher.

        Args:
            key (str): Alphabetic string, length must be a perfect square.
        Returns:
            numpy.ndarray: n x n matrix of integers (A=0..Z=25).
        Raises:
            InvalidKeyError: If key length is not a perfect square, not alphabetic, or matrix is not invertible mod 26.
        """
        key = key.upper()
        L = len(key)
        n = int(math.sqrt(L))
        if n < 2 or n * n != L or not key.isalpha():
            raise InvalidKeyError("Key for Hill cipher must be a perfect square length (e.g., 4, 9, 16) and alphabetic.")
        nums = [ord(c) - ord('A') for c in key]
        matrix = np.array(nums).reshape(n, n)
        det = int(round(np.linalg.det(matrix)))
        if det == 0 or self._modinv(det, 26) is None:
            raise InvalidKeyError("Key matrix is not invertible modulo 26.")
        return matrix

    def _modinv(self, a, m):
        """
        Compute the modular inverse of a modulo m using the extended Euclidean algorithm.

        Args:
            a (int): Value to invert.
            m (int): Modulus.
        Returns:
            int or None: Modular inverse if exists, else None.
        """
        a = a % m
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

    def _process_text(self, text: str, n: int):
        text = ''.join([c.upper() for c in text if c.isalpha()])
        pad = (-len(text)) % n
        if pad:
            text += 'X' * pad
        return text

    def encrypt(self, plaintext: str, key: str) -> str:
        matrix = self._key_to_matrix(key)
        n = matrix.shape[0]
        text = self._process_text(plaintext, n)
        result = ''
        for i in range(0, len(text), n):
            block = [ord(c) - ord('A') for c in text[i:i+n]]
            enc = np.dot(matrix, block) % 26
            result += ''.join(chr(num + ord('A')) for num in enc)
        return result

    def decrypt(self, ciphertext: str, key: str) -> str:
        matrix = self._key_to_matrix(key)
        n = matrix.shape[0]
        det = int(round(np.linalg.det(matrix)))
        det_inv = self._modinv(det, 26)
        if det_inv is None:
            raise InvalidKeyError("Key matrix is not invertible modulo 26.")
        # Compute matrix of cofactors
        cofactors = np.zeros_like(matrix)
        for r in range(n):
            for c in range(n):
                minor = np.delete(np.delete(matrix, r, axis=0), c, axis=1)
                cof = ((-1) ** (r + c)) * int(round(np.linalg.det(minor)))
                cofactors[r, c] = cof
        adjugate = cofactors.T % 26
        inv_matrix = (det_inv * adjugate) % 26
        text = self._process_text(ciphertext, n)
        result = ''
        for i in range(0, len(text), n):
            block = [ord(c) - ord('A') for c in text[i:i+n]]
            dec = np.dot(inv_matrix, block) % 26
            result += ''.join(chr(int(num) + ord('A')) for num in dec)
        return result 