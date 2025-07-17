import unittest
from ciphers.substitution import SubstitutionCipher
from ciphers import InvalidKeyError

class TestSubstitutionCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = SubstitutionCipher()
        self.key = 'QWERTYUIOPASDFGHJKLZXCVBNM'

    def test_encrypt(self):
        self.assertEqual(self.cipher.encrypt('Hello', self.key), 'Itssg')
        self.assertEqual(self.cipher.encrypt('abc', self.key), 'qwe')

    def test_decrypt(self):
        self.assertEqual(self.cipher.decrypt('Itssg', self.key), 'Hello')
        self.assertEqual(self.cipher.decrypt('qwe', self.key), 'abc')

    def test_invalid_key(self):
        with self.assertRaises(InvalidKeyError):
            self.cipher.encrypt('Hello', 'QWERTY')
        with self.assertRaises(InvalidKeyError):
            self.cipher.decrypt('Hello', 'QWERTY')
        with self.assertRaises(InvalidKeyError):
            self.cipher.encrypt('Hello', 'QWERTYUIOPASDFGHJKLZXCVBNQ')  # repeated letter

    def test_empty_string(self):
        self.assertEqual(self.cipher.encrypt('', self.key), '')
        self.assertEqual(self.cipher.decrypt('', self.key), '')

if __name__ == '__main__':
    unittest.main() 