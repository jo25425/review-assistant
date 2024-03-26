# review-assistant
_Review writing assistant (final project from Le Wagon Machine Learning Bootcamp)_

## Application description

1. _Input 1_: The user provides a title or description for the product they want to review.
2. _Inference 1_: Given this product description, our application generates a list of criteria to rate.
3. _Input 2_: The user provides a rating for whichever criteria they'd like.
4. _Inference 2_: Given the rated criteria, our application generates a few possible reviews.

## Criteria and review generation API

This API is built with FastAPI and served via uvicorn.
To run it locally, navigate to the root of this repository and run:
```bash
uvicorn reviewassistant.api.fast:app --reload
```

## Application frontend

The frontend will be built and served with Streamlit and deployed to Streamlit cloud.
