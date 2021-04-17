FROM python:3.8-slim

ENV PYTHONPATH=/popular-repos

RUN mkdir -p /popular-repos

WORKDIR /popular-repos

ADD ./services/health_check/application /popular-repos/services/health_check/application
ADD ./services/health_check/requirements.txt /popular-repos/services/health_check/requirements.txt

RUN pip install -r /popular-repos/services/health_check/requirements.txt

ENTRYPOINT python /popular-repos/services/health_check/application
