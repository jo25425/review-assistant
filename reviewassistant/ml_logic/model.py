import os

import requests
from langchain.callbacks.streaming_stdout_final_only import \
    FinalStreamingStdOutCallbackHandler
from langchain.chains import RetrievalQA
from langchain.chains.retrieval_qa.base import BaseRetrievalQA
from langchain_community.llms import GPT4All
from langchain_core.language_models.base import BaseLanguageModel
from langchain_openai import ChatOpenAI,  OpenAI
from langchain.prompts import PromptTemplate

from reviewassistant.params import MODEL_DIR, OPENAI_API_KEY

GPT4ALL_MODELS_URL = "https://gpt4all.io/models/gguf/"

def download_gpt4all_model(model_name: str, model_path: str):
    url = GPT4ALL_MODELS_URL + model_name
    response = requests.get(url, stream=True)

    with open(model_path, mode='wb') as out:
        for chunk in response.iter_content(chunk_size=10 * 1024):
            out.write(chunk)


def load_model(mode: str, model_name: str):

    # OpenAI
    if mode == 'openai':
        llm = ChatOpenAI(model_name=model_name, openai_api_key=OPENAI_API_KEY)
        return llm

    # Local
    if mode == 'local':
        model_path = os.path.join(MODEL_DIR, model_name)

        if not os.path.exists(model_path) \
            and os.path.isfile(model_path):
            download_gpt4all_model(model_name, model_path)

        callbacks = [FinalStreamingStdOutCallbackHandler()]
        llm = GPT4All(model=model_path, callbacks=callbacks, verbose=True)
        return llm


def build_chain(model: BaseLanguageModel, vector_db) -> BaseRetrievalQA:
    qa = RetrievalQA.from_chain_type(
        llm=model,
        chain_type="stuff",
        retriever=vector_db.as_retriever(search_kwargs={"k": 1}),
        return_source_documents=False,
        verbose=False,
    )
    return qa

def load_model_review(model_name: str):
    llm = OpenAI(model_name=model_name, openai_api_key=OPENAI_API_KEY, temperature=0.9)
    return llm


def load_prompt(input_variables: str, template: str):
    prompt = PromptTemplate(
            input_variables = input_variables,
            template = template
            )
    return prompt
