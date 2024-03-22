from reviewassistant.ml_logic.embedder import embed_text
from reviewassistant.ml_logic.model import load_model, build_chain
from reviewassistant.params import *
from langchain_core.language_models.base import BaseLanguageModel

from reviewassistant.utils import parse_criteria


def generate_criteria(product_txt: str, model: BaseLanguageModel) -> list[str]:
    vector_db = embed_text(product_txt, MODE_STEP_1)
    chain = build_chain(model, vector_db)
    result = chain.invoke(PROMPT).get('result')
    criteria = parse_criteria(result)
    return criteria

def generate_reviews(rated_criteria: dict[str, int], model: BaseLanguageModel, num_reviews: int=3) -> str:
    pass


if __name__ == '__main__':
    product = input("Which product would you like a review for?\n ")

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
    llm_step_2 = None  #TODO Reuse if same as before, otherwise load
    reviews = generate_reviews(rated_criteria)

    print("\nHere are some potential reviews:")
    for i, review in enumerate(reviews):
        if i > 0:
            print("---\n")
        print(review + '\n')
