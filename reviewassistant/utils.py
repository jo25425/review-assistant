def parse_criteria(text: str, verbose: bool=False) -> list[str]:
    """Given a block of text containing criteria, attempt to extract these
    criteria.
    """
    lines = text.strip().split('\n')
    criteria = lines if len(lines) > 1 else lines[0].split(', ')
    cleaned_criteria = [c[3:] if c[0].isnumeric() else c for c in criteria]

    if verbose:
        print(f"Attempting to parse '{text}'")
        print(f"-> {len(lines)} lines")
        print(f"-> criteria:", criteria)
        print(f"-> criteria cleaned:", cleaned_criteria)

    return cleaned_criteria
