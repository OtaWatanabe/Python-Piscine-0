def count_in_list(lst: list[str], match: str) -> int:
    """Count the number of the string match in lst, list of strings"""
    count = 0
    for obj in lst:
        if obj == match:
            count += 1
    return count
