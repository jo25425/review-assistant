# review-assistant
_Review writing assistant (final project from Le Wagon Machine Learning Bootcamp)_

## API description

This API is implemented with the FastAPI framework and provides 2 endpoints: 

* `criteria`:
  Given a product title or description, returns a list of relevant criteria that could be rated by a user.

* `reviews`:
  Given the original product description and the rated criteria (a dictionary associating each of the criteria to a score), returns several possible reviews.

Additionally, the following endpoint is automatically provided by FastAPI:

* `docs`: Serves a web UI describing the API available and allowing to try it out interactively.

## Deployment

#### Local

This API is built with FastAPI and served via uvicorn. You'll need to make a copy of the
file `.env.sample` called `.env` and add a valid OpenAI key in order to run it.

To run it **locally**, navigate to the root of this repository and run:
```bash
uvicorn reviewassistant.api.fast:app --reload
```

#### Containerised

 ℹ️ The image is around 2.5GB, but if you're getting memory errors, build it for a smaller GPT4 model than the one selected by default (see list by scrolling down on the [GPT4All page](https://gpt4all.io/index.html)).

🚨 To run in Docker, you'll need to allow containers to use at least 14Gi of RAM (add Swap memory too in order to make better use of your resources).
 
To run it **locally in a Docker container**, make sure to have the Docker daemon running and build the image:
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

#### GCP (Google CLoud Platform)

_(Documentation coming soon...)_

## Application frontend

The frontend is built with Streamlit and deployed to Streamlit cloud.

-  Repository: [review-assistant-website](https://github.com/jo25425/review-assistant-website)
-  App: [review-writing-assistant.streamlit.app](https://review-writing-assistant.streamlit.app/)
