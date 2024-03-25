from reviewassistant.ml_logic.embedder import embed_text
from reviewassistant.ml_logic.model import load_model, build_chain
from reviewassistant.params import *
from langchain_core.language_models.base import BaseLanguageModel

from reviewassistant.utils import parse_criteria

from reviewassistant.ml_logic.prompt import input_variable
from reviewassistant.ml_logic.model import load_model_review, load_prompt


def generate_criteria(product_txt: str, model: BaseLanguageModel) -> list[str]:
    vector_db = embed_text(product_txt, MODE_STEP_1)
    chain = build_chain(model, vector_db)
    result = chain.invoke(PROMPT_1).get('result')
    criteria = parse_criteria(result)
    return criteria

def generate_reviews(product_name: str, rated_criteria: dict[str, int], model: BaseLanguageModel, num_reviews: int=5) -> str:

    criteria = [{"0":"Very bad", "1":"Bad", "2":"Not so good", "3":"Acceptable", "4":"Good", "5":"Very good"}]

    prefix = []
    Rated_Criteria = []
    rated_adjectives = []

    for key, value in rated_criteria[0].items():
        Rated_Criteria.append(key)
        rated_adjectives.append(criteria[0][str(rated_criteria[0][key])])
        pref = f"{key}:{criteria[0][str(rated_criteria[0][key])]}"
        prefix.append(pref)

    template = f" You are a costumer. I want you to generate a product review on {product_name}\
            considering the following criteria: {prefix}. Be precised and concised."


    criteria_list, adjective_list = [f"criteria_{n}" for n in range(len(rated_criteria[0]))],\
                                                  [f"adjective_{n}" for n in range(len(rated_criteria[0]))]

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
    #product = input("Which product would you like a review for?\n ")

    # # First inference
    # llm_step_1 = load_model(mode=MODE_STEP_1, model_name=MODEL_NAME_STEP_1)
    # criteria = generate_criteria(product, llm_step_1)

    # print("\nRate the following from 1 to 5:")
    # rated_criteria = {
    #     criterium: int(input(f"{criterium.title()}? "))
    #     for criterium in criteria
    # }
    # print(rated_criteria)

    product = "jeans"

    rated_criteria = [{"Design": 0, "Comfort": 1, "Durability": 2, "Fit": 3, "Price": 4 }]

    # Second inference
    llm_step_2 = load_model_review(model_name=MODEL_NAME_STEP_2, openai_key = OPENAI_API_KEY)
    reviews = generate_reviews(product, rated_criteria, llm_step_2)

    print(reviews)
    # print("\nHere are some potential reviews:")
    # for i, review in enumerate(reviews):
    #     if i > 0:
    #         print("---\n")
    #     print(review + '\n')
