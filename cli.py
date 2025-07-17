import argparse
from ciphers.caesar import CaesarCipher
from ciphers.vigenere import VigenereCipher
from ciphers.playfair import PlayfairCipher
from ciphers.substitution import SubstitutionCipher
from ciphers.hill import HillCipher
from ciphers import InvalidKeyError
import sys

CIPHERS = {
    'caesar': CaesarCipher(),
    'vigenere': VigenereCipher(),
    'playfair': PlayfairCipher(),
    'substitution': SubstitutionCipher(),
    'hill': HillCipher(),
}

EXAMPLES = '''\nExamples:\n  python cli.py caesar encrypt --text "Hello, World!" 3\n  python cli.py vigenere decrypt --text "Rijvs, Uyvjn!" key\n  python cli.py playfair encrypt --text "Hide the gold" keyword\n  python cli.py substitution encrypt --text "Hello" QWERTYUIOPASDFGHJKLZXCVBNM\n  python cli.py hill encrypt --text "HELP" HILL\n  python cli.py caesar encrypt --input-file input.txt --output-file output.txt 5\n  python cli.py vigenere encrypt --text "Hello" --text "World" key --verbose\n'''

def parse_args():
    parser = argparse.ArgumentParser(
        description='Classical Ciphers CLI',
        epilog=EXAMPLES,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('cipher', choices=CIPHERS.keys(), help='Cipher to use')
    parser.add_argument('mode', choices=['encrypt', 'decrypt'], help='Mode')
    parser.add_argument('text', nargs='?', default=None, help='Text to process (or use --text-list/--input-file)')
    parser.add_argument('key', help='Cipher key')
    parser.add_argument('--text-list', nargs='+', help='Multiple texts to process (space or comma separated)')
    parser.add_argument('--input-file', help='Input file path')
    parser.add_argument('--output-file', help='Output file path')
    parser.add_argument('--delimiter', default=',', help='Delimiter for batch text (default: ,)')
    parser.add_argument('--verbose', action='store_true', help='Show detailed cipher process')
    args = parser.parse_args()
    
    # Validate input sources
    input_sources = sum(1 for x in [args.text, args.text_list, args.input_file] if x is not None)
    if input_sources == 0:
        parser.error("One of text, --text-list, or --input-file is required")
    if input_sources > 1:
        parser.error("Only one of text, --text-list, or --input-file can be used")
    return args

def process_texts(cipher, mode, texts, key, verbose):
    results = []
    for text in texts:
        try:
            if not text:
                continue  # Skip empty texts
            if mode == 'encrypt':
                output = cipher.encrypt(text, key)
            else:
                output = cipher.decrypt(text, key)
            if verbose:
                print(f"[VERBOSE] Cipher: {cipher.__class__.__name__}, Key: {key}, Input: {text}, Output: {output}")
            results.append((text, output))
        except InvalidKeyError as e:
            print(f"Error: {e}", file=sys.stderr)
            results.append((text, None))
    return results

def main():
    args = parse_args()
    cipher = CIPHERS[args.cipher]
    
    # Gather input texts
    texts = []
    if args.text_list:
        for t in args.text_list:
            texts.extend([s for s in t.split(args.delimiter) if s])
    elif args.input_file:
        try:
            with open(args.input_file, 'r', encoding='utf-8') as f:
                texts = [line.rstrip('\n') for line in f if line.strip()]
        except Exception as e:
            print(f"Error reading input file: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.text:
        texts = [args.text]
    else:
        print("No input text provided.", file=sys.stderr)
        sys.exit(1)
    
    # Process
    results = process_texts(cipher, args.mode, texts, args.key, args.verbose)
    
    # Output
    output_lines = []
    for inp, out in results:
        if out is not None:
            output_lines.append(f"Input: {inp} -> Output: {out}")
        else:
            output_lines.append(f"Input: {inp} -> Error: Invalid key")
    output = '\n'.join(output_lines)
    if args.output_file:
        try:
            with open(args.output_file, 'w', encoding='utf-8') as f:
                f.write(output + '\n')
        except Exception as e:
            print(f"Error writing output file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(output)

if __name__ == '__main__':
    main()