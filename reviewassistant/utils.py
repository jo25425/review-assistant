def parse_criteria(text: str) -> list[str]:
    """Given a block of text containing criteria, one per line, returns the list
    of criteria. These are usually preceded by some numbering in the model
    responses, so we strip the first 3 characters (digit, dot or bracket, and
    space)."""
    return [line[3:] for line in text.split('\n')[:10] if line]
