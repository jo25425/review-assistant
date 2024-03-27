from reviewassistant.params import MAX_CRITERIA, PROMPT_2


def strip_non_alpha(text: str) -> str:
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

        cleaned_criteria = [strip_non_alpha(c) for c in criteria]
        debug_str += f"-> criteria cleaned: {cleaned_criteria}"
    except:
        print(debug_str)
        raise ValueError

    return list(filter(None, cleaned_criteria))[:MAX_CRITERIA]

def parse_reviews(text: str) -> list[str]:
    """Given a block of text containing multiple reviews, attempts to separate
    these reviews.
    """
    lines = text.strip().split('\n')
    reviews = []
    current_review = ""

    def add_current_review():
        nonlocal current_review
        if current_review:
            reviews.append(current_review)
            current_review = ""

    for i, line in enumerate(lines):
        # Strip the line from a potential review title
        if line.startswith("Review"):
            line = strip_non_alpha(line[7:])

        # If the line isn't empty now, then we add it to the current review
        # being "read"
        if not line.strip() == "":
            current_review += strip_non_alpha(line)
        # Otherwise it means the review we were reading is over
        else:
            add_current_review()

        # If it's the last line, the last review is over
        if i == len(lines) - 1:
            add_current_review()

    return reviews


def build_reviews_input(product: str, rated_criteria: dict[str, int]) -> str:
    txt = ""
    for criterium, rating in rated_criteria.items():
        criterium = criterium.lower()
        if rating >= 4:
            txt += f"The {product} excels in {criterium} as it offers exceptional {criterium}.\n"
        elif rating >= 3:
            txt += f"The {product} performs well in terms of {criterium} with {criterium} that meets expectations.\n"
        elif rating >= 2:
            txt += f"The {product} has average {criterium}, providing satisfactory {criterium}.\n"
        else:
            txt += f"The {product} could improve its {criterium} as the current {criterium} is below expectations.\n"
    return txt
