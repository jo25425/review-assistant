from reviewassistant.ml_logic.embedder import embed_text
from reviewassistant.ml_logic.model import load_model, build_chain, invoke
from reviewassistant.params import *
from langchain_core.language_models.base import BaseLanguageModel

from reviewassistant.utils import parse_criteria


def generate_criteria(product_txt: str, model: BaseLanguageModel) -> list[str]:
    vector_db = embed_text(product_txt, MODE_STEP_1)
    chain = build_chain(model, vector_db)
    result = invoke(chain, PROMPT_1)
    criteria = parse_criteria(result)
    return criteria


def generate_reviews(product: str, rated_criteria: dict[str, int], model: BaseLanguageModel, num_reviews: int=NUM_REVIEWS) -> str:
    for criteria, rating in rated_criteria.items():
        if rating >= 4:
            PROMPT_2 += f"The {product} excels in {criteria.lower()} as it offers exceptional {criteria.lower()}.\n"
        elif rating >= 3:
            PROMPT_2 += f"The {product} performs well in terms of {criteria.lower()} with {criteria.lower()} that meet expectations.\n"
        elif rating >= 2:
            PROMPT_2 += f"The {product} has average {criteria.lower()}, providing satisfactory {criteria.lower()}.\n"
        else:
            PROMPT_2 += f"The {product} could improve its {criteria.lower()} as the current {criteria.lower()} is below expectations.\n"

    vector_db = embed_text(product, rated_criteria, MODE_STEP_2)
    chain = build_chain(model, vector_db)
    result = chain.invoke(PROMPT_2).get('result')
    return result


if __name__ == '__main__':
    # product = input("Which product would you like a review for?\n ")
    product = "iphone 15"
    print('')

    # First inference
    llm_step_1 = load_model(mode=MODE_STEP_1, model_name=MODEL_NAME_STEP_1)
    criteria = generate_criteria(product, llm_step_1)

    print("\nRate the following from 1 to 5:")
    rated_criteria = {
        criterium: int(input(f"{criterium.title()}? "))
        for criterium in criteria
    }
    print(rated_criteria)

    # Second inference
    # Linda's modifications
    llm_step_2 = load_model(mode=MODE_STEP_2, model_name=MODEL_NAME_STEP_2)  #TODO Reuse if same as before, otherwise load
    reviews = generate_reviews(product, rated_criteria, llm_step_2)

    print("\nHere are some potential reviews:")
    for i, review in enumerate(reviews):
        if i > 0:
            print("---\n")
        print(review + '\n')
