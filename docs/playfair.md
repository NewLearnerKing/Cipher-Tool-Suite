# Playfair Cipher

## History
The Playfair cipher was invented in 1854 by Charles Wheatstone but is named after Lord Playfair, who promoted its use. It is a digraph substitution cipher that encrypts pairs of letters using a 5x5 grid generated from a keyword.

## How It Works (Math)
- The 5x5 grid is filled with the keyword (no repeated letters), then the remaining letters of the alphabet (I/J are combined).
- Plaintext is split into pairs (digraphs). If a pair has identical letters, insert 'X' between them. If the plaintext has an odd number of letters, append 'X' at the end.
- For each pair:
  - If both letters are in the same row: replace each with the letter to its right (wrap around).
  - If both are in the same column: replace each with the letter below it (wrap around).
  - Otherwise: replace each with the letter in its own row and the column of the other letter.

## Example Usage

### Encrypt
```
python cli.py playfair encrypt --text "Hide the gold" keyword
# Output: Input: HIDETHEGOLD -> Output: BMNDZBXDKYBE
```

### Decrypt
```
python cli.py playfair decrypt --text "BMNDZBXDKYBE" keyword
# Output: Input: BMNDZBXDKYBE -> Output: HIDETHEGOLDX
```

## Key Format
- The key must be an alphabetic string (e.g., keyword).
- Non-alphabetic keys will result in an error. 