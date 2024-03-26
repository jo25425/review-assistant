FROM langchain/langchain

WORKDIR /prod

RUN pip install --upgrade pip

COPY requirements_prod.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install --upgrade langchain langchain-community langchain-core

COPY reviewassistant reviewassistant
COPY setup.py setup.py
RUN pip install .

CMD uvicorn reviewassistant.api.fast:app --host 0.0.0.0 --port $PORT
