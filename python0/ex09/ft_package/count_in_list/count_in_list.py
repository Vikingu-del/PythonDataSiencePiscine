def count_in_list(lst: list[str], item: str) -> int:
    """
    This function finds the occurencess of a string
    item inside a list of strings
    """
    return len([x for x in lst if x == item])
