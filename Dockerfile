FROM langchain/langchain

WORKDIR /prod

COPY requirements_prod.txt requirements.txt
RUN pip install -r requirements.txt

COPY reviewassistant reviewassistant
COPY setup.py setup.py
RUN pip install .

CMD uvicorn reviewassistant.api.fast:app --host 0.0.0.0 --port $PORT
