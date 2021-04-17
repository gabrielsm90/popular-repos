Popular Github Repositories
===========================

The Popular Github Repositories is a service designed to
check if a given repository in Github is popular or not.

A repository is popular if it has a score >= 500 given that
the score is calculated by the Repository's  Number of Stars
multiplied by 1 plus the Repository's number of forks.

It's a web application presenting the endpoint 
`/{user_name}/{repo_name}`.

## Technology Stack

### Programming Language

`Python 3.8`

#### Frameworks and libs

`Flask` to serve the app.

`requests` to fetch the Github API.

`pytest` for unit testing.

### Packaging

`Docker`

### Code Quality Checks

`Flake8` for linting.

`Black` for formatting.

## Development

### Setting up the environment

### Pre-requisites

- Docker
- Docker Compose
- Python 3.8
- pip

#### Environment Variables

To run and test the application, you must set your Github
access token in an environment variable.

- GITHUB_ACCESS_TOKEN = Your token to access the Github API

#### Requirements

Install the requirements with:

```
pip install -r requirements.txt && pip install -r requirements-dev.txt
```

### Running the application automated tests

In the Project's folder, run:

```
pytest --cov-report term-missing --cov=application tests/`
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
