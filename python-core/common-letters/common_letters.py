def common_letters(left: str, right: str) -> str:
    result = []
    seen = set()
    for ch in left:
      if ch in right and ch not in seen:
        result.append(ch)
        seen.add(ch)
    return "".join(result)