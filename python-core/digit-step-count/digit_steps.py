def count_digit_steps(text: str) -> int:
    count = 0
    for i in range(len(text) - 1):
        actual = text[i]
        siguiente = text[i + 1]

        if text[i].isdigit() and text[i + 1].isdigit():
            if int(text[i]) < int(text[i + 1]):
                count += 1
    return count

