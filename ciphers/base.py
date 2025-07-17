from abc import ABC, abstractmethod

class Cipher(ABC):
    """Abstract base class for all ciphers."""

    @abstractmethod
    def encrypt(self, plaintext: str, key: str) -> str:
        pass

    @abstractmethod
    def decrypt(self, ciphertext: str, key: str) -> str:
        pass 