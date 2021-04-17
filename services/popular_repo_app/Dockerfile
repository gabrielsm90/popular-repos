FROM python:3.8-slim

ENV PYTHONPATH=/popular-repos

RUN mkdir -p /popular-repos

WORKDIR /popular-repos

ADD ./services/popular_repo_app/application /popular-repos/services/popular_repo_app/application
ADD ./services/popular_repo_app/requirements.txt /popular-repos/services/popular_repo_app/requirements.txt

RUN pip install -r /popular-repos/services/popular_repo_app/requirements.txt

ENTRYPOINT python /popular-repos/services/popular_repo_app/application
