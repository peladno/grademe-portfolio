def merge_sorted_values(left: list[int], right: list[int]) -> list[int]:
    result = []
    merge = [*left, *right]

    while merge:
      smallest = min(merge)
      result.append(smallest)
      merge.remove(smallest)
    return result