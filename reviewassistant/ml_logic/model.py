from datetime import datetime
import os
import requests
from langchain.callbacks.streaming_stdout_final_only import \
    FinalStreamingStdOutCallbackHandler
from langchain.cache import InMemoryCache
from langchain.chains import RetrievalQA
from langchain.chains.retrieval_qa.base import BaseRetrievalQA
from langchain.globals import set_llm_cache
from langchain_community.llms import GPT4All
from langchain_core.language_models.base import BaseLanguageModel
from langchain_openai import ChatOpenAI

from reviewassistant.params import MODEL_DIR, OPENAI_API_KEY


GPT4ALL_MODELS_URL = "https://gpt4all.io/models/gguf/"


# set_llm_cache(InMemoryCache())
os.makedirs(MODEL_DIR, exist_ok=True)


def download_gpt4all_model(model_name: str, model_path: str):
    url = GPT4ALL_MODELS_URL + model_name
    response = requests.get(url, stream=True)

    os.makedirs(MODEL_DIR, exist_ok=True)
    with open(model_path, mode='wb') as out:
        for chunk in response.iter_content(chunk_size=10 * 1024):
            out.write(chunk)


def load_model(mode: str, model_name: str):
    print("Loading model...", end=' ')

    # OpenAI
    if mode == 'openai':
        llm = ChatOpenAI(model_name=model_name, openai_api_key=OPENAI_API_KEY)
        print("✅")
        return llm

    # Local
    if mode == 'local':
        model_path = os.path.join(MODEL_DIR, model_name)

        if not (os.path.exists(model_path) \
            and os.path.isfile(model_path)):
            download_gpt4all_model(model_name, model_path)

        callbacks = [FinalStreamingStdOutCallbackHandler()]
        llm = GPT4All(model=model_path, callbacks=callbacks, verbose=True)

        print("✅")
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

def invoke(chain: BaseRetrievalQA, prompt: str) -> str:
    start_time = datetime.now()
    print("Generating criteria...", end=' ')
    result = chain.invoke(prompt).get('result', '')
    print(f"✅ ({(datetime.now() - start_time).total_seconds():.2f}s)")
    return result
