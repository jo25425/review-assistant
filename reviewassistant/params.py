import os

##################  VARIABLES  ##################

HG_EMBEDDING_MODEL = os.environ.get('HG_EMBEDDING_MODEL')

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
OPENAI_MODEL = os.environ.get('OPENAI_MODEL')

MODE_STEP_1 = os.environ.get('MODE_STEP_1')
MODEL_NAME_STEP_1 = os.environ.get('MODEL_NAME_STEP_1')

MODE_STEP_2 = os.environ.get('MODE_STEP_2')
MODEL_NAME_STEP_2 = os.environ.get('MODEL_NAME_STEP_2')

PROMPT_1 = "Given this product title, please select between 3 and 6 criteria to rate in order to compose a product review. No need to explain the criteria."

##################  CONSTANTS  ##################
MODEL_DIR = "models"
CHROMA_PERSIST_DIR = os.path.join('db', 'chroma_3')
