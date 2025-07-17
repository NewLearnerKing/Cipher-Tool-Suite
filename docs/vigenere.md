# Vigenère Cipher

## History
The Vigenère cipher is a polyalphabetic substitution cipher invented by Giovan Battista Bellaso in the 16th century and later misattributed to Blaise de Vigenère. It was considered unbreakable for centuries due to its use of multiple Caesar ciphers based on a keyword.

## How It Works (Math)
- Each letter in the plaintext is shifted by an amount determined by the corresponding letter of a repeating keyword.
- The transformation can be described mathematically as:

  `E(x, k) = (x + y) mod 26`
  
  Where:
  - `E(x, k)` is the encrypted letter
  - `x` is the position of the plaintext letter (0 for A, 1 for B, ...)
  - `y` is the position of the key letter (0 for A, 1 for B, ...)

## Example Usage

### Encrypt
```
python cli.py vigenere encrypt --text "ATTACKATDAWN" LEMON
# Output: Input: ATTACKATDAWN -> Output: LXFOPVEFRNHR
```

### Decrypt
```
python cli.py vigenere decrypt --text "LXFOPVEFRNHR" LEMON
# Output: Input: LXFOPVEFRNHR -> Output: ATTACKATDAWN
```

### File Input/Output
```
python cli.py vigenere encrypt --input-file input.txt --output-file output.txt key
```

## Key Format
- The key must be an alphabetic string (e.g., LEMON).
- Non-alphabetic keys will result in an error. 