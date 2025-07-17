import unittest
from ciphers.playfair import PlayfairCipher
from ciphers import InvalidKeyError

class TestPlayfairCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = PlayfairCipher()

    def test_encrypt(self):
        self.assertEqual(self.cipher.encrypt('Hide the gold', 'keyword'), 'BMNDZBXDKYBE')
        self.assertEqual(self.cipher.encrypt('balloon', 'playfair'), 'IBSUPMNA')

    def test_decrypt(self):
        self.assertEqual(self.cipher.decrypt('BMNDZBXDKYBE', 'keyword'), 'HIDETHEGOLDX')
        self.assertEqual(self.cipher.decrypt('IBSUPMNA', 'playfair'), 'BALLOONX')

    def test_invalid_key(self):
        with self.assertRaises(InvalidKeyError):
            self.cipher.encrypt('Hello', '1234')
        with self.assertRaises(InvalidKeyError):
            self.cipher.decrypt('Hello', '')

    def test_empty_string(self):
        self.assertEqual(self.cipher.encrypt('', 'keyword'), '')
        self.assertEqual(self.cipher.decrypt('', 'keyword'), '')

if __name__ == '__main__':
    unittest.main() 