# Substitution Cipher

## History
The monoalphabetic substitution cipher is a classical cipher where each letter in the plaintext is replaced by a letter with a fixed mapping. The mapping can be random or user-defined. It is more secure than the Caesar cipher but still vulnerable to frequency analysis.

## How It Works (Math)
- The key is a permutation of the alphabet (26 unique letters).
- Each letter in the plaintext is replaced by the corresponding letter in the key mapping.
- Encryption: substitute each letter using the mapping.
- Decryption: reverse the mapping.

## Example Usage

### Encrypt
```
python cli.py substitution encrypt --text "Hello" QWERTYUIOPASDFGHJKLZXCVBNM
# Output: Input: Hello -> Output: Itssg
```

### Decrypt
```
python cli.py substitution decrypt --text "Itssg" QWERTYUIOPASDFGHJKLZXCVBNM
# Output: Input: Itssg -> Output: Hello
```

## Key Format
- The key must be 26 unique alphabetic characters (e.g., QWERTYUIOPASDFGHJKLZXCVBNM).
- Keys with repeated or missing letters will result in an error. 