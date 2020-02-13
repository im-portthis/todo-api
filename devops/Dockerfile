FROM python:3.7

WORKDIR /opt/project

COPY Pipfile Pipfile.lock ./
RUN pip install -U pip && \
    pip install pipenv && \
    pipenv install --system --deploy

COPY ./src .
COPY ./src/entrypoint.sh .
RUN chmod +x ./entrypoint.sh

EXPOSE 8000
