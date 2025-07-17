import unittest
from ciphers.caesar import CaesarCipher
from ciphers import InvalidKeyError

class TestCaesarCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = CaesarCipher()

    def test_encrypt(self):
        self.assertEqual(self.cipher.encrypt('ABC', '3'), 'DEF')
        self.assertEqual(self.cipher.encrypt('xyz', '2'), 'zab')
        self.assertEqual(self.cipher.encrypt('Hello, World!', '5'), 'Mjqqt, Btwqi!')

    def test_decrypt(self):
        self.assertEqual(self.cipher.decrypt('DEF', '3'), 'ABC')
        self.assertEqual(self.cipher.decrypt('zab', '2'), 'xyz')
        self.assertEqual(self.cipher.decrypt('Mjqqt, Btwqi!', '5'), 'Hello, World!')

    def test_invalid_key(self):
        with self.assertRaises(InvalidKeyError):
            self.cipher.encrypt('Hello', 'abc')
        with self.assertRaises(InvalidKeyError):
            self.cipher.decrypt('Hello', 'abc')

    def test_empty_string(self):
        self.assertEqual(self.cipher.encrypt('', '3'), '')
        self.assertEqual(self.cipher.decrypt('', '3'), '')

if __name__ == '__main__':
    unittest.main() 