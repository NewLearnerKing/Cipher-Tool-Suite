import unittest
from ciphers.hill import HillCipher
from ciphers import InvalidKeyError

class TestHillCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = HillCipher()

    def test_encrypt(self):
        self.assertEqual(self.cipher.encrypt('HELP', 'HILL'), 'ZEBB')
        self.assertEqual(self.cipher.encrypt('ACT', 'GYBN'), 'POH')  # 'ACTX' -> 'POH'

    def test_decrypt(self):
        self.assertEqual(self.cipher.decrypt('ZEBB', 'HILL'), 'HELP')
        self.assertEqual(self.cipher.decrypt('POH', 'GYBN'), 'ACTX')

    def test_invalid_key_length(self):
        with self.assertRaises(InvalidKeyError):
            self.cipher.encrypt('HELP', 'ABC')
        with self.assertRaises(InvalidKeyError):
            self.cipher.decrypt('HELP', 'ABCDE')

    def test_non_alpha_key(self):
        with self.assertRaises(InvalidKeyError):
            self.cipher.encrypt('HELP', '1234')

    def test_non_invertible_matrix(self):
        # 'AAAA' matrix is not invertible mod 26
        with self.assertRaises(InvalidKeyError):
            self.cipher.encrypt('HELP', 'AAAA')

    def test_odd_length_input(self):
        # Should pad with 'X'
        self.assertEqual(self.cipher.encrypt('HI', 'HILL'), self.cipher.encrypt('HIX', 'HILL'))
        self.assertEqual(self.cipher.decrypt('ZEB', 'HILL'), self.cipher.decrypt('ZEBX', 'HILL'))

    def test_empty_string(self):
        self.assertEqual(self.cipher.encrypt('', 'HILL'), '')
        self.assertEqual(self.cipher.decrypt('', 'HILL'), '')

if __name__ == '__main__':
    unittest.main() 