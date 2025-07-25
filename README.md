# Ciphers

A Python collection of classical cryptographic ciphers with a command-line interface (CLI) and GUI. Designed for educational purposes, modularity, and easy extension.

## Installation

```sh
pip install -r requirements.txt
```

## Usage

### CLI

Encrypt or decrypt text using any supported cipher:

```sh
python cli.py caesar encrypt --text "Hello, World!" 3
python cli.py vigenere decrypt --text "Rijvs, Uyvjn!" key
python cli.py playfair encrypt --text "Hide the gold" keyword
python cli.py substitution encrypt --text "Hello" QWERTYUIOPASDFGHJKLZXCVBNM
python cli.py hill encrypt --text "HELP" HILL
python cli.py hill encrypt --text "EXAMPLE" HILLMAGICX  # 3x3 key example
```

### GUI

Launch the graphical interface:

```sh
python gui.py
```

#### GUI Features
- **Cipher selection, text/key input, encrypt/decrypt, and result display**
- **Copy to Clipboard**: Copy the result with one click
- **File Input/Output**: Load text from a file and save results to a file
- **History Panel**: View recent encryptions/decryptions
- **Educational Visualization**:
  - Playfair: See the 5x5 grid for the current key
  - Hill: See the key matrix for the current key (supports any nxn size)

## Key Formats

- **Caesar:** Integer (e.g., 3). Non-integer keys will result in an error.
- **Vigenère:** Alphabetic string (e.g., key). Non-alphabetic keys will result in an error.
- **Playfair:** Alphabetic string (e.g., keyword). Non-alphabetic keys will result in an error.
- **Substitution:** 26 unique alphabetic characters (e.g., QWERTYUIOPASDFGHJKLZXCVBNM). Must not repeat letters.
- **Hill:** Alphabetic string of perfect square length (e.g., 4, 9, 16, ...). Key must form an invertible matrix mod 26. (e.g., HILL for 2x2, HILLMAGICX for 3x3)

## Extending the Project

- Add new ciphers in the `ciphers/` directory, inheriting from `Cipher` in `base.py`.
- Register new ciphers in `cli.py` and `gui.py`.
- Add corresponding unit tests in `tests/`.
- Add documentation in the `docs/` folder.

## Running Tests

Run all unit tests and check coverage:

```sh
pytest --cov=ciphers
```

---

For more details, see the cipher-specific docs in the `docs/` folder.
