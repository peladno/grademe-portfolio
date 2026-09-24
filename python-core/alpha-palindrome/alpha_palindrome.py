def is_alpha_palindrome(text: str) -> bool:
    checker = "".join(c.lower() for c in text if c.isalpha())

    if not checker:
        return False
    
    return checker == checker[::-1]