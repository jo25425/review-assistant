import os

#TODO Get variables from .env file

##################  VARIABLES  ##################
MODE = 'local'
MODEL_NAME = 'mistral-7b-openorca.gguf2.Q4_0.gguf'
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

##################  CONSTANTS  ##################
MODEL_DIR = "models"
