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

## ML inference

The text-based ML tasks performed by the application are implemented using the [LangChain](https://python.langchain.com/docs/get_started/introduction/) framework. Each of these is a Retrieval QA (Question Answering) task, where the "documents" are actually just the product description (to generate criteria) or the description and rated criteria (to generate reviews). This enables the LLM (Large Language Model) powering the task to distinguish between a question (prompt) and a context, which - based on results from the experimental phase of this project - results in equal or better performance to a simple QA task, while speeding up the processing time (since the vectorised descriptions can be cached).

The user input is embedded by a model thanks to HuggingFace's [sentence-transformers](https://huggingface.co/sentence-transformers) library. This model, defined as an environment variable, can be much smaller than the one performing the inference, so long as it is compatible with [GPT4All](https://docs.gpt4all.io/index.html). This is important because GPT4All is the library used to load the models that the tasks will use.

Two different types of LLMs are used, each demonstrating a different speed vs. cost trade-off:
- 🐢 _Local LLMs_: These GPT-type models are available publicly and can be loaded by GPT4All at **no cost**. The speed of inference depends on the size of the model and the specifications of the system the application is running on. For a MacBook Pro suitable for programming or a single mid-size instance on GCP, this would be **slow**, between 30 and 60 seconds.
- 🐇 _ChatGPT API_: This API is provided by OpenAI and utilises one of the latest ChatGPT models, but it is **paid for**. Since it is built for heavy usage by a very large number of users, it is backed by suitable architecture and therefore **fast**, taking a few seconds only (after embedding).

> [!NOTE]
> The default configuration sets the `criteria` endpoint to use a local LLM (**slow**) and the `reviews` endpoint to use the ChatGPT API (**fast**).

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

> [!TIP]
> To run in Docker, you'll need to allow containers to use at least 14Gi of RAM (add Swap memory too in order to make better use of your resources).
 
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

Instructions and commands for deploying this application as a service on GCP's Cloud Run can be found in the file [deployment_commands.txt](deployment_commands.txt).

## Application frontend

The frontend is built with Streamlit and deployed to Streamlit cloud.

-  Repository: [review-assistant-website](https://github.com/jo25425/review-assistant-website)
-  App: [review-writing-assistant.streamlit.app](https://review-writing-assistant.streamlit.app/)
