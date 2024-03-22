from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from reviewassistant.interface.main import generate_criteria, generate_reviews
from reviewassistant.ml_logic.model import load_model
from reviewassistant.params import *


app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    # allow_methods=["*"],  # Allows all methods
    # allow_headers=["*"],  # Allows all headers
)

# Preload models for computing speed
app.state.model1 = load_model(MODE_STEP_1, MODEL_NAME_STEP_1)
app.state.model_2 = (app.state.model1
                     if MODE_STEP_1 == MODE_STEP_2 and MODEL_NAME_STEP_1 == MODEL_NAME_STEP_2 else
                     load_model(MODE_STEP_2, MODEL_NAME_STEP_2))


@app.get("/criteria")
def get_criteria(product: str) -> list[str]:
    criteria = generate_criteria(product, app.state.model1)
    return criteria


@app.get("/reviews")
def get_reviews(rated_criteria: dict[str, int]) -> list[str]:
    reviews = generate_reviews(rated_criteria, app.state.model2)
    return reviews


@app.get("/")
def root():
    return dict(greeting="Hello")
