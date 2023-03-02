FROM python:3.10

WORKDIR code/

RUN curl -sSL https://install.python-poetry.org | python3 -

COPY pyproject.toml pyproject.toml

COPY poetry.lock poetry.lock

RUN ln -s $HOME/.local/bin/poetry /usr/bin/poetry

RUN poetry config virtualenvs.create false

RUN poetry install

COPY . .