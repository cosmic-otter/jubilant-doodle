FROM python:3.9

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY source/ .

CMD ["uvicorn", "handler:app", "--host", "0.0.0.0", "--port", "3000"]