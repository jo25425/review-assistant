import os

from langchain_openai import ChatOpenAI
from langchain.callbacks.streaming_stdout_final_only import FinalStreamingStdOutCallbackHandler
from langchain.llms import GPT4All

from reviewassistant.params import MODEL_DIR, OPENAI_API_KEY

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
            pass  # Download file

        callbacks = [FinalStreamingStdOutCallbackHandler()]
        llm = GPT4All(model=model_path, callbacks=callbacks, verbose=True)
        return llm
