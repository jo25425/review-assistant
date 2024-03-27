from reviewassistant.ml_logic.embedder import embed_text
from reviewassistant.ml_logic.model import load_model, build_chain, invoke
from reviewassistant.params import *
from langchain_core.language_models.base import BaseLanguageModel

from reviewassistant.utils import build_reviews_input, parse_criteria, parse_reviews


def generate_criteria(product_txt: str, model: BaseLanguageModel) -> list[str]:
    vector_db = embed_text(product_txt, MODE_STEP_1)
    chain = build_chain(model, vector_db)
    result = invoke(chain, PROMPT_1)
    criteria = parse_criteria(result)
    return criteria


def generate_reviews(product: str, rated_criteria: dict[str, int], model: BaseLanguageModel) -> str:
    reviews_input = build_reviews_input(product, rated_criteria)
    vector_db = embed_text(reviews_input, MODE_STEP_2)
    chain = build_chain(model, vector_db)
    result = invoke(chain, PROMPT_2)
    reviews = parse_reviews(result)
    return reviews


if __name__ == '__main__':
    product = input("Which product would you like a review for?\n ")
    print('')

    # First inference
    llm_step_1 = load_model(mode=MODE_STEP_1, model_name=MODEL_NAME_STEP_1)
    criteria = generate_criteria(product, llm_step_1)

    print("\nRate the following from 1 to 5:")
    rated_criteria = {
        criterium: int(input(f"{criterium.title()}? "))
        for criterium in criteria
    }
    print('')

    # Second inference
    llm_step_2 = (llm_step_1
                  if MODE_STEP_1 == MODE_STEP_2 and MODEL_NAME_STEP_1 == MODEL_NAME_STEP_2 else
                  load_model(MODE_STEP_2, MODEL_NAME_STEP_2))
    reviews = generate_reviews(product, rated_criteria, llm_step_2)

    print("\nHere are some potential reviews:\n")
    for i, review in enumerate(reviews):
        if i > 0:
            print("---\n")
        print(review + '\n')
