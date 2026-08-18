def is_alpha_palindrome(text: str) -> bool:
    letters = "".join(c for c in text if c.isalpha())

    if not letters:
        return False

    cleaned = letters.lower()
    
    return (cleaned == cleaned[::-1])