import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from reviewassistant.interface.main import generate_criteria, generate_reviews
from reviewassistant.ml_logic.model import load_model
from reviewassistant.params import *


# Preload models for computing speed
model_1 = load_model(MODE_STEP_1, MODEL_NAME_STEP_1)
model_2 = (model_1
           if MODE_STEP_1 == MODE_STEP_2 and MODEL_NAME_STEP_1 == MODEL_NAME_STEP_2 else
           load_model(MODE_STEP_2, MODEL_NAME_STEP_2))

app = FastAPI()
app.state.model_1 = model_1
app.state.model_2 = model_2

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
)


@app.get("/criteria")
def get_criteria(product: str) -> list[str]:
    criteria = generate_criteria(product, app.state.model_1)
    return criteria


@app.post("/reviews")
def get_reviews(product: str, rated_criteria: str) -> list[str]:
    rated_criteria = json.loads(rated_criteria)
    reviews = generate_reviews(product, rated_criteria, app.state.model_2)
    return reviews


@app.get("/")
def root() -> str:
    return "Hello from your review writing assistant :)"
