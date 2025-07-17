import unittest
from ciphers.vigenere import VigenereCipher
from ciphers import InvalidKeyError

class TestVigenereCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = VigenereCipher()

    def test_encrypt(self):
        self.assertEqual(self.cipher.encrypt('ATTACKATDAWN', 'LEMON'), 'LXFOPVEFRNHR')
        self.assertEqual(self.cipher.encrypt('hello', 'abc'), 'hfnlp')
        self.assertEqual(self.cipher.encrypt('Hello, World!', 'key'), 'Rijvs, Uyvjn!')

    def test_decrypt(self):
        self.assertEqual(self.cipher.decrypt('LXFOPVEFRNHR', 'LEMON'), 'ATTACKATDAWN')
        self.assertEqual(self.cipher.decrypt('hfnlp', 'abc'), 'hello')
        self.assertEqual(self.cipher.decrypt('Rijvs, Uyvjn!', 'key'), 'Hello, World!')

    def test_invalid_key(self):
        with self.assertRaises(InvalidKeyError):
            self.cipher.encrypt('Hello', '123')
        with self.assertRaises(InvalidKeyError):
            self.cipher.decrypt('Hello', '123')
        with self.assertRaises(InvalidKeyError):
            self.cipher.encrypt('Hello', '')
        with self.assertRaises(InvalidKeyError):
            self.cipher.decrypt('Hello', '')

    def test_empty_string(self):
        self.assertEqual(self.cipher.encrypt('', 'abc'), '')
        self.assertEqual(self.cipher.decrypt('', 'abc'), '')

if __name__ == '__main__':
    unittest.main() 