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

To run it in Docker, make sure to have the Docker daemon running and build the image:
```bash
docker build --tag=$GAR_IMAGE:dev .
```
Then you can access its shell with:
```bash
docker run -it -e PORT=8000 -p 8000:8000 $GAR_IMAGE:dev sh
```

And finally, to run it:
```bash
docker run -e PORT=8000 -p 8000:8000 --env-file $GAR_IMAGE:dev
```


## Application frontend

The frontend will be built and served with Streamlit and deployed to Streamlit cloud.
