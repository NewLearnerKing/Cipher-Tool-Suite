class InvalidKeyError(Exception):
    """Raised when a cipher key is invalid."""
    pass

class InvalidTextError(Exception):
    """Raised when input text is invalid for a cipher."""
    pass

def preserve_case(char: str, result: str) -> str:
    return result.upper() if char.isupper() else result.lower() 