def delimiters_balanced(text: str) -> bool:
    pairs = {
        ')':'(',
        ']':'[',
        '}':'{'
    }

    delimiters = []

    for c in text:
        if c in pairs.values():
            delimiters.append(c)
        elif c in pairs:
            if not delimiters:
                return False
            if delimiters.pop() != pairs[c]:
                return False

    return len(delimiters) == 0
