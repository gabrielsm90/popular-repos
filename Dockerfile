FROM python:3.8-slim

ENV PYTHONPATH=/popular-repos

RUN mkdir -p /popular-repos

WORKDIR /popular-repos

ADD ./application /popular-repos/application
ADD requirements.txt /popular-repos/requirements.txt

RUN pip install -r /popular-repos/requirements.txt

ENTRYPOINT python /popular-repos/application
