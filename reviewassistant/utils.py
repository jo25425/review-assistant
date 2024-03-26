# def parse_criteria(text: str) -> list[str]:
#     """Given a block of text containing criteria, one per line, returns the list
#     of criteria. These are usually preceded by some numbering in the model
#     responses, so we strip the first 3 characters (digit, dot or bracket, and
#     space)."""
#     return [line[3:] for line in text.split('\n')[:10] if line]

# def parse_criteria(text: str, verbose: bool=False) -> list[str]:
#     """Given a block of text containing criteria, attempt to extract these
#     criteria.
#     """
#     lines = text.strip().split('\n')
#     criteria = lines if len(lines) > 1 else lines[0].split(', ')
#     cleaned_criteria = [c[3:] if c[0].isnumeric() else c for c in criteria]

#     if verbose:
#         print(f"Attempting to parse '{text}'")
#         print(f"-> {len(lines)} lines")
#         print(f"-> criteria:", criteria)
#         print(f"-> criteria cleaned:", cleaned_criteria)

#     return cleaned_criteria
from reviewassistant.params import MAX_CRITERIA


def clean_criterium(text: str) -> str:
    '''Strips non-letters from the beginning of the string and spaces from the
    end.'''
    while len(text) and not text[0].isalpha():
        text = text[1:]
    return text.strip()

def parse_criteria(text: str) -> list[str]:
    """Given a block of text containing criteria, attempt to extract these
    criteria.
    """
    debug_str = f"Attempting to parse '{text}'"

    try:
        lines = text.strip().split('\n')
        debug_str += f"-> {len(lines)} lines"

        criteria = lines if len(lines) > 1 else lines[0].split(', ')
        debug_str += f"-> criteria: {criteria}"

        cleaned_criteria = [clean_criterium(c) for c in criteria]
        debug_str += f"-> criteria cleaned: {cleaned_criteria}"
    except:
        print(debug_str)
        raise ValueError

    return list(filter(None, cleaned_criteria))[:MAX_CRITERIA]
