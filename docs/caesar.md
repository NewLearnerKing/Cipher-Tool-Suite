# Caesar Cipher

## History
The Caesar cipher is one of the oldest known encryption techniques, named after Julius Caesar, who reportedly used it to communicate with his generals. It is a type of substitution cipher in which each letter in the plaintext is shifted by a fixed number of positions down the alphabet.

## How It Works (Math)
- Each letter is replaced by the letter a fixed number of positions (the key) further down the alphabet.
- For example, with a shift of 3: A → D, B → E, C → F, etc.
- The transformation can be described mathematically as:

  `E(x) = (x + k) mod 26`
  
  Where:
  - `E(x)` is the encrypted letter
  - `x` is the position of the plaintext letter (0 for A, 1 for B, ...)
  - `k` is the key (shift)

## Example Usage

### Encrypt
```
python cli.py caesar encrypt --text "HELLO" 3
# Output: Input: HELLO -> Output: KHOOR
```

### Decrypt
```
python cli.py caesar decrypt --text "KHOOR" 3
# Output: Input: KHOOR -> Output: HELLO
```

### File Input/Output
```
python cli.py caesar encrypt --input-file input.txt --output-file output.txt 5
```

## Key Format
- The key must be an integer (e.g., 3).
- Non-integer keys will result in an error. 