from .base import Cipher
from . import InvalidKeyError
import string

class PlayfairCipher(Cipher):
    """Playfair cipher implementation."""

    def __init__(self):
        self.size = 5

    def _generate_square(self, key: str):
        """
        Generate a 5x5 Playfair square from the keyword.

        Args:
            key (str): Alphabetic keyword.
        Returns:
            list[list[str]]: 5x5 matrix as a list of lists.
        Raises:
            InvalidKeyError: If key is not alphabetic or is empty.
        """
        key = ''.join([c.upper() for c in key if c.isalpha()])
        if not key:
            raise InvalidKeyError("Key for Playfair cipher must be alphabetic.")
        seen = set()
        square = []
        for c in key + string.ascii_uppercase:
            if c == 'J':
                c = 'I'
            if c not in seen:
                seen.add(c)
                square.append(c)
            if len(square) == 25:
                break
        return [square[i:i+self.size] for i in range(0, 25, self.size)]

    def _find_position(self, square, char):
        for i, row in enumerate(square):
            for j, c in enumerate(row):
                if c == char:
                    return i, j
        raise ValueError(f"Character {char} not found in Playfair square.")

    def _process_text(self, text):
        text = ''.join([c.upper() for c in text if c.isalpha()])
        processed = ''
        i = 0
        while i < len(text):
            a = text[i]
            b = text[i+1] if i+1 < len(text) else 'X'
            if a == b:
                processed += a + 'X'
                i += 1
            else:
                processed += a + b
                i += 2
        if len(processed) % 2 != 0:
            processed += 'X'
        return processed

    def encrypt(self, plaintext: str, key: str) -> str:
        square = self._generate_square(key)
        text = self._process_text(plaintext)
        result = ''
        for i in range(0, len(text), 2):
            a, b = text[i], text[i+1]
            row_a, col_a = self._find_position(square, a)
            row_b, col_b = self._find_position(square, b)
            if row_a == row_b:
                result += square[row_a][(col_a+1)%5] + square[row_b][(col_b+1)%5]
            elif col_a == col_b:
                result += square[(row_a+1)%5][col_a] + square[(row_b+1)%5][col_b]
            else:
                result += square[row_a][col_b] + square[row_b][col_a]
        return result

    def decrypt(self, ciphertext: str, key: str) -> str:
        square = self._generate_square(key)
        text = ''.join([c.upper() for c in ciphertext if c.isalpha()])
        result = ''
        for i in range(0, len(text), 2):
            a, b = text[i], text[i+1]
            row_a, col_a = self._find_position(square, a)
            row_b, col_b = self._find_position(square, b)
            if row_a == row_b:
                result += square[row_a][(col_a-1)%5] + square[row_b][(col_b-1)%5]
            elif col_a == col_b:
                result += square[(row_a-1)%5][col_a] + square[(row_b-1)%5][col_b]
            else:
                result += square[row_a][col_b] + square[row_b][col_a]
        return result 