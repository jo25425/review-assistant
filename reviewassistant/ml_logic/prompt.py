
#input variables for PromptTemplate()
def input_variable(product_name: str, criteria_list,  adjective_list,  feeling_list=None,  **kwargs):
    if feeling_list is not None:
        input_var = [f"{product_name}"] + criteria_list + adjective_list + feeling_list
    else:
        input_var = [f"{product_name}"] + criteria_list + adjective_list

    return input_var
