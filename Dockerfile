# 2.53GB image
FROM langchain/langchain

WORKDIR /prod

COPY requirements_prod.txt requirements.txt

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir --timeout 120 -r requirements.txt
RUN pip install --upgrade langchain langchain-community langchain-core


COPY reviewassistant reviewassistant
COPY setup.py setup.py
RUN pip install .

CMD uvicorn reviewassistant.api.fast:app --host 0.0.0.0 --port $PORT
