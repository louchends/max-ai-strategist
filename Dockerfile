FROM python:3.10-slim

RUN apt-get update && apt-get install -y git

WORKDIR /app

COPY . .

ENV PYTHONPATH="${PYTHONPATH}:/app"

RUN pip install openai langchain

CMD ["python", "main.py"]
