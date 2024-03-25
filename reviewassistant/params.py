import os

##################  VARIABLES  ##################

MAX_CRITERIA = int(os.environ.get('MAX_CRITERIA'))
NUM_REVIEWS = int(os.environ.get('NUM_REVIEWS'))

HG_EMBEDDING_MODEL = os.environ.get('HG_EMBEDDING_MODEL')

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
OPENAI_MODEL = os.environ.get('OPENAI_MODEL')

MODE_STEP_1 = os.environ.get('MODE_STEP_1')
MODEL_NAME_STEP_1 = os.environ.get('MODEL_NAME_STEP_1')

MODE_STEP_2 = os.environ.get('MODE_STEP_2')
MODEL_NAME_STEP_2 = os.environ.get('MODEL_NAME_STEP_2')

PROMPT_1 = f"Given this product title, please select between 3 and {MAX_CRITERIA}" \
    " criteria to rate in order to compose a product review. No explanation," \
    " no example."

##################  CONSTANTS  ##################
MODEL_DIR = "models"
CHROMA_PERSIST_DIR = os.path.join('db', 'chroma_3')
