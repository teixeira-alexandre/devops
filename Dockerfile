FROM python:3.12

WORKDIR /app

RUN pip install fastapi uvicorn pytest httpx

COPY main.py /app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]