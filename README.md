Popular Github Repositories
===========================

The Popular Github Repositories is a service designed to
check if a given repository in Github is popular or not.

A repository is popular if it has a score >= 500 given that
the score is calculated by the Repository's  Number of Stars
multiplied by 1 plus the Repository's number of forks.

It's a web application presenting the endpoint 
`/{user_name}/{repository_name}`.

## Technology Stack

### Programming Language

`Python 3.8`

#### Frameworks and libs

`Flask` to serve the app.

`requests` to fetch the Github API.

`apscheduler` to run the health checker.

`pytest` for unit testing.

### Packaging

`Docker`

### Code Quality Checks

`Flake8` for code linting.

`Black` for code formatting.

## Project's Structure

```
popular-repos
├── docs
│   ├── popular_repos.yaml
├── services
│   ├── health_check
│       ├── application
│       │       ├── __init__.py
│       │       ├── __main__.py
│       │       ├── api_client.py
│       │       ├── config.py
│       ├── tests
│       │       ├── __init__.py
│       │       ├── test_scheduler.py
│   ├── popular_repo_app
│       ├── application
│       │   ├── controllers
│       │       ├── __init__.py
│       │       ├── health.py
│       │       ├── repositories.py
│       │   ├── service
│       │       ├── __init__.py
│       │       ├── evaluator.py
│       │       ├── exceptions.py
│       │       ├── github_client.py
│       │   ├── __init__.py
│       │   ├── __main__.py
│       │   ├── app.py
│       │   ├── config.py
│       ├── tests
│       │   ├── __init__.py
│       │   ├── test_application.py
│       ├── Dockerfile
│       ├── requirements.txt
├── .coveragerc
├── .flake8
├── .gitignore
├── docker-compose.yml
├── README.md
├── requirements-dev.txt
```

The `docs` folder holds the OAS documentation for the
web application.

`services` is where one will find the two services of 
this project, the Web App that is used and exposed and
the Health Checker.

In the two services folder, one will find the same structure
of a folder dedicated to the application, one folder with the
automated tests, a Dockerfile for the service and the
requirements for it.

Still on the top level, we have two configuration files:

- .coveragerc: Configuration for the test coverage.
- .flake8: Configuration for the code linter.

The file `docker-compose.yml` is used to spin up the services
with Docker.

Finally, a `requirements-dev.txt` so that the developer
won't need to install requirements from different requirements
files to have the development environment in place.

## Development

### Setting up the environment

### Pre-requisites

- Docker
- Docker Compose
- Python 3.8
- pip

#### Environment Variables

To run and test the application, you must set two environment
variables.

#### Github Access Token

The application fetches data from Github's API, so you
need to set your credential in the env var GITHUB_ACCESS_TOKEN.

- GITHUB_ACCESS_TOKEN = Your token to access the Github API
  
#### Python Path

As a Python developer, you most certainly already have that
env variable. So, here, you will need to add the path to
the folder `popular-repos` inside your project.

If you are running the tests from Pycharm IDE, it will take
this step automatically for you.

#### Requirements

As a developer in this project, you will only need to
install the requirements in the file `requirements-dev.txt`.

This way we concentrate all the required libs in one file,
but when deploying, Docker will only install the required
libs for each microservice using the services specific
requirement files.

```
pip install -r requirements-dev.txt
```

### Running the project's automated tests

We have two services in this project. 

To run automated tests for the web application, go to the
project's folder and run:

```
pytest --cov-report term-missing --cov=services\popular_repo_app\application services\popular_repo_app\tests\
```

And to run the tests of the health check, also in the project's
folder:

```
pytest --cov-report term-missing --cov=services\health_check\application services\health_check\tests\
```

### Running the application locally

To run the application locally, from the project's folder, 
run the following command:

```
docker-compose up -d --build
```

Once you run this command, you can access application in
http://localhost:5000/ and the API documentation in 
http://localhost:5001/

## Next Steps

The next steps in this project may be tackled in two groups.

### Improvements of the current features

To improve the application but without a change in the
current features, two improvements would immediately 
follow the current scenario.

- Add Caching layer to the Web App endpoints.
- Integrate a logging tool to the Health Checker, such
  as ELK, so that the Error alarms would be easily 
  accessible.
  
### New features

As an improvement of features, there could be a mechanism
that would store the results calculated by the REST service
in a dedicated database.

With the data stored, it would be possible to use Data Science
and Machine Learning to get insights from the data.

Things like "which repo is being queried a lot", "how long would
it take to a repo become Popular since the first query", "how
likely is a specific repo to become popular in the next X days"
etc.