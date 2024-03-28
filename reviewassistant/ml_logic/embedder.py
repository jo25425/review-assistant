from hashlib import sha1
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema.document import Document
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from reviewassistant.params import *


def get_persist_directory(text: str, model_name: str) -> str:
    embeddings_id = os.path.basename(model_name) + '-' + text
    id_hash = sha1((embeddings_id).encode()).hexdigest()
    return os.path.join(CHROMA_PERSIST_DIR, id_hash)


def extract_documents(text: str) -> list[Document]:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = [Document(page_content=x) for x in text_splitter.split_text(text)]
    return docs

def embed_text(text: str, mode: str) -> list[Document]:
    print("Embedding text...", end=' ', flush=True)

    docs = extract_documents(text)

    if mode == 'openai':
        embedder = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        persist_dir = get_persist_directory(text, 'openai')
    else:
        embedder = HuggingFaceEmbeddings(model_name=HG_EMBEDDING_MODEL)
        persist_dir = get_persist_directory(text, HG_EMBEDDING_MODEL)

    vector_db = Chroma.from_documents(
        docs,
        embedder,
        persist_directory=persist_dir
    )
    print("✅")
    return vector_db
