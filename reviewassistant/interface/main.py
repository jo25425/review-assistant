from reviewassistant.ml_logic.embedder import embed_text
from reviewassistant.ml_logic.model import load_model, build_chain, invoke, load_model_review, load_prompt
from reviewassistant.ml_logic.prompt import input_variable
from reviewassistant.params import *
from langchain_core.language_models.base import BaseLanguageModel

from reviewassistant.utils import parse_criteria


def generate_criteria(product_txt: str, model: BaseLanguageModel) -> list[str]:
    vector_db = embed_text(product_txt, MODE_STEP_1)
    chain = build_chain(model, vector_db)
    result = invoke(chain, PROMPT_1)
    criteria = parse_criteria(result)
    return criteria


def generate_reviews(product_name: str, rated_criteria: dict[str, int], model: BaseLanguageModel, num_reviews: int=NUM_REVIEWS) -> str:

    criteria = [{"0":"Very bad", "1":"Bad", "2":"Not so good", "3":"Acceptable", "4":"Good", "5":"Very good"}]

    prefix = []
    Rated_Criteria = []
    rated_adjectives = []

    for key, value in rated_criteria.items():
        Rated_Criteria.append(key)
        rated_adjectives.append(criteria[0][str(rated_criteria[key])])
        pref = f"{key}:{criteria[0][str(rated_criteria[key])]}"
        prefix.append(pref)

    template = f" You are a costumer. I want you to generate a product review on {product_name}\
            considering the following criteria: {prefix}. Be precised and concised."


    criteria_list, adjective_list = [f"criteria_{n}" for n in range(len(rated_criteria))],\
                                                  [f"adjective_{n}" for n in range(len(rated_criteria))]

    input_variables = input_variable(product_name, criteria_list,  adjective_list)

    llm = model
    prompt = load_prompt(input_variables, template)
    response = llm(prompt.format(criteria_0 = Rated_Criteria[0], criteria_1 = Rated_Criteria[1],\
                                criteria_2 = Rated_Criteria[2], criteria_3 = Rated_Criteria[3],
                                criteria_4 = Rated_Criteria[4], adjective_0 = rated_adjectives[0],\
                                adjective_1 = rated_adjectives[1], adjective_2 = rated_adjectives[2],\
                                adjective_3 = rated_adjectives[3], adjective_4 = rated_adjectives[4])
                          )
    return response


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
    llm_step_2 = load_model_review(model_name=MODEL_NAME_STEP_2, openai_key=OPENAI_API_KEY)
    reviews = generate_reviews(product, rated_criteria, llm_step_2)
    print(reviews)

    # print("\nHere are some potential reviews:")
    # for i, review in enumerate(reviews):
    #     if i > 0:
    #         print("---\n")
    #     print(review + '\n')
