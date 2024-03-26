import os

#TODO Get variables from .env file

##################  VARIABLES  ##################

HG_EMBEDDING_MODEL = 'sentence-transformers/all-MiniLM-L6-v2'

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
OPENAI_MODEL = 'gpt-3.5-turbo'

MODE_STEP_1 = 'local'
MODEL_NAME_STEP_1 = 'mistral-7b-openorca.gguf2.Q4_0.gguf'

MODE_STEP_2 = 'openai'
MODEL_NAME_STEP_2 = "gpt-3.5-turbo-instruct"

PROMPT_1 = "Given this product title, please select between 3 and 6 criteria to rate in order to compose a product review. No need to explain the criteria."

##################  CONSTANTS  ##################
MODEL_DIR = "models"
CHROMA_PERSIST_DIR = os.path.join('db', 'chroma_3')

MAX_CRITERIA = 5
