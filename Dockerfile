#Etapa 1
FROM python:3.12-slim AS builder

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_HOME="/opt/poetry"

RUN pip install poetry
ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN python -m venv .venv && \
    poetry install --only main --no-root


#Etapa 2
FROM python:3.12-slim AS runner


RUN groupadd -r pomodoro && useradd -r -g pomodoro pomodoro

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
COPY . .


RUN chown -R pomodoro:pomodoro /app

ENV PATH="/app/.venv/bin:$PATH"


USER pomodoro

CMD ["gunicorn", "wsgi:app", "--bind", "0.0.0.0:8000"]