import os

#TODO Get variables from .env file

##################  VARIABLES  ##################
MODE = 'local'

HG_EMBEDDING_MODEL = 'sentence-transformers/all-MiniLM-L6-v2'

GPT4ALL_MODEL_NAME = 'mistral-7b-openorca.gguf2.Q4_0.gguf'

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
OPENAI_MODEL = 'gpt-3.5-turbo'

##################  CONSTANTS  ##################
MODEL_DIR = "models"
CHROMA_PERSIST_DIR = os.path.join('db', 'chroma_3')
