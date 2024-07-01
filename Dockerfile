FROM python:3

RUN mkdir app
WORKDIR ./app
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY *.py ./
COPY ./static ./static
COPY ./templates ./templates
RUN mkdir output

ENTRYPOINT flask --app flask_app run --host=0.0.0.0
