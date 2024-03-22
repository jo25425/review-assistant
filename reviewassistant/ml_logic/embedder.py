from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema.document import Document
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from reviewassistant.params import *


def extract_documents(text) -> list[Document]:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = [Document(page_content=x) for x in text_splitter.split_text(text)]
    return docs

def embed_documents(texts, model_name) -> list[Document]:
    if model_name == 'openai':
        embedder = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    else:
        embedder = HuggingFaceEmbeddings(model_name=model_name)

    vector_db = Chroma.from_documents(
        texts,
        embedder,
        persist_directory=CHROMA_PERSIST_DIR + model_name
    )
    return vector_db
