import os

##################  VARIABLES  ##################

MAX_CRITERIA = int(os.environ.get('MAX_CRITERIA'))
NUM_REVIEWS = int(os.environ.get('NUM_REVIEWS'))

HG_EMBEDDING_MODEL = os.environ.get('HG_EMBEDDING_MODEL')

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

MODE_STEP_1 = os.environ.get('MODE_STEP_1')
MODEL_NAME_STEP_1 = os.environ.get('MODEL_NAME_STEP_1')

MODE_STEP_2 = os.environ.get('MODE_STEP_2')
MODEL_NAME_STEP_2 = os.environ.get('MODEL_NAME_STEP_2')

PROMPT_1 = f"Given this product title, please select between 3 and {MAX_CRITERIA}" \
    " criteria to rate in order to compose a review for this product. One per line."

PROMPT_2 = f"Based on the given product title and ratings provided, generate {NUM_REVIEWS}" \
    " review(s) for this product. Write them from the perspective of someone" \
    " who has bought the product without being too informal and without" \
    " explicitly referring to the fact that the review is based on a rating or" \
    " provided information. At least 4 sentences."

##################  CONSTANTS  ##################
MODEL_DIR = "models"
CHROMA_PERSIST_DIR = os.path.join('db', 'chroma_3')
