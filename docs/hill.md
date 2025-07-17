# Hill Cipher

## History
The Hill cipher, invented by Lester S. Hill in 1929, is a polygraphic substitution cipher based on linear algebra. It uses matrix multiplication to encrypt blocks of letters, making it one of the first ciphers to use more advanced mathematics.

## How It Works (Math)
- The key is a square matrix (e.g., 2x2, 3x3, etc.) derived from a keyword of perfect square length.
- Plaintext is split into blocks of n letters, converted to numbers (A=0, ..., Z=25).
- Each block is multiplied by the key matrix modulo 26 to produce ciphertext.
- Decryption uses the inverse of the key matrix modulo 26.

## Example Usage

### Encrypt (2x2)
```
python cli.py hill encrypt --text "HELP" HILL
# Output: Input: HELP -> Output: ZEBB
```

### Encrypt (3x3)
```
python cli.py hill encrypt --text "EXAMPLE" HILLMAGICX
# Output: ...
```

### Decrypt
```
python cli.py hill decrypt --text "ZEBB" HILL
# Output: Input: ZEBB -> Output: HELP
```

## Key Format
- The key must be an alphabetic string of perfect square length (e.g., 4, 9, 16, ...).
- The matrix must be invertible modulo 26 (not all keys are valid).
- Non-invertible or non-alphabetic keys will result in an error.

## GUI Visualization
- The GUI displays the Hill key matrix for the current key, supporting any nxn size. 