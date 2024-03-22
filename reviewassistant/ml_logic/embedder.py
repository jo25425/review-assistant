from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema.document import Document
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from reviewassistant.params import *


def extract_documents(text: str) -> list[Document]:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = [Document(page_content=x) for x in text_splitter.split_text(text)]
    return docs

def embed_text(text: str, mode: str) -> list[Document]:
    docs = extract_documents(text)

    if mode == 'openai':
        embedder = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    else:
        embedder = HuggingFaceEmbeddings(model_name=HG_EMBEDDING_MODEL)

    persist_dir = os.path.join(CHROMA_PERSIST_DIR, HG_EMBEDDING_MODEL)
    vector_db = Chroma.from_documents(
        docs,
        embedder,
        persist_directory=persist_dir
    )
    return vector_db
