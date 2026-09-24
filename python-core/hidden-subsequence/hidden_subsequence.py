def is_subsequence(sub, text):
    i = 0

    for char in text:
        if i < len(sub) and sub[i] == char:
            i += 1

    return i == len(sub)