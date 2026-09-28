def zigzag_letters(text: str) -> str:
    result = ""
    changed = False

    for c in text:
        if c.isalpha():
            if changed:
                result += c.upper()
            else:
                result += c.lower()

            changed = not changed
        else:
            result += c
    return result