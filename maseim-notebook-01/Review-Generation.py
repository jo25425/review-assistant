import os
import sys
from dotenv import load_dotenv
load_dotenv()

from langchain import PromptTemplate
from langchain.llms import OpenAI

def ReviewGeneration(product_name, input_criteria_score : dict) -> None:
    """
    This function expects a dictionary of the form:
    input_criteria_score = [{"criteria_0":score_0}, {"criteria_1":score_1}, ...., {"criteria_n":score_n}]
    if not, this function returns None.
    """
    # Global Variables
    N = len(input_criteria_score[0]) #number of criteria

    # transforming score into adjectives
    criteria = [{"0":"Very bad", "1":"Bad", "2":"Not so good", "3":"Acceptable", "4":"Good", "5":"Very good"}]

    # Decompressing input_criteria_score dictionary
    prefix = []
    input_criteria = []
    input_adjectives = []
    for key, value in input_criteria_score[0].items():
        input_criteria.append(key)
        input_adjectives.append(criteria[0][str(input_criteria_score[0][key])])
        pref = f"{key}:{criteria[0][str(input_criteria_score[0][key])]}"
        prefix.append(pref)

    # Criteria, Adjective and Feeling lists
    criteria_list, adjective_list, feeling_list = [f"criteria_{n}" for n in range(N)],\
                                                  [f"adjective_{n}" for n in range(N)],\
                                                  [f"feeling_{n}" for n in range(N)]


    # template for PromptTemplate()
    def template(prefix):
        """
            This function build a template with a set of instructions to be passed to the model.
        """
        temp = f" You are a costumer. I want you to generate a product review on {product_name}\
               considering the following criteria: {prefix}. Be precise and concise."

        return temp

    template = template(prefix)

    #input variables for PromptTemplate()
    def input_variable(product_name, criteria_list,  adjective_list,  feeling_list=None,  **kwargs):
        """
            This function builds the input_variables necessary for the PromptTemplate()
            Here, we have made feeling_list optional. input_variable() can be called without it!
        """
        if feeling_list is not None:
            input_var = [f"{product_name}"] + criteria_list + adjective_list + feeling_list
        else:
            input_var = [f"{product_name}"] + criteria_list + adjective_list

        return input_var

    #instantiating input_variable()
    input_variables = input_variable(product_name, criteria_list,  adjective_list)

    #instantiating the model
    llm = OpenAI(temperature=0.9)

    # building the prompt
    prompt = PromptTemplate(
        input_variables = input_variables,
        template = template
            )
    def Prompt(**kwargs):
        if N == 1:
            response = llm(prompt.format(criteria_0=input_criteria[0], adjective_0=input_adjectives[0])
                          )
        if N == 2:
            response = llm(prompt.format(criteria_0=input_criteria[0], criteria_1=input_criteria[1],
                          adjective_0=input_adjectives[0], adjective_1=input_adjectives[1])
                          )
        if N == 3:
            response = llm(prompt.format(criteria_0=input_criteria[0], criteria_1=input_criteria[1], criteria_2=input_criteria[2],\
                          adjective_0=input_adjectives[0], adjective_1=input_adjectives[1], adjective_2=input_adjectives[2])
                          )
        if N == 4:
            response = llm(prompt.format(criteria_0=input_criteria[0], criteria_1=input_criteria[1], criteria_2=input_criteria[2], criteria_3=input_criteria[3],\
                          adjective_0=input_adjectives[0], adjective_1=input_adjectives[1], adjective_2=input_adjectives[2], adjective_3=input_adjectives[3])
                          )
        if N == 5:
            response = llm(prompt.format(criteria_0=input_criteria[0], criteria_1=input_criteria[1], criteria_2=input_criteria[2], criteria_3=input_criteria[3], criteria_4=input_criteria[4],\
                          adjective_0=input_adjectives[0], adjective_1=input_adjectives[1], adjective_2=input_adjectives[2], adjective_3=input_adjectives[3], adjective_4=input_adjectives[4])
                          )

        return response

    review_generation = Prompt()
    return review_generation
