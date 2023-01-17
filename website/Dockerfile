FROM python:3.9

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY source/ .

CMD ["uvicorn", "handler:app", "--host", "ks3.dev.hrl.internal", "--port", "3000"]