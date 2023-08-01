FROM python:3.10-bullseye

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install "poetry==1.4.2"
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false --local
RUN poetry install --no-ansi --only main

COPY blog .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000
