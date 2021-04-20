"""
Module to test the Flask application.

For this microservice, an E2E testing approach was taken
and, because of that, we have a few important gains when
it comes to test coverage:

- Meaningful metric. When you test from end to end and
mock only third party applications, your test coverage
gives you a clear picture of what's being properly
tested because you know that the flows are not being
triggered by mocked functions with biased inputs. One
should keep in mind that pytest coverage shows exactly
which lines are not being tested.

- Flow control. By triggering the application in the way
that it will be used in production (or close to it), the
test coverage might help you find flows that are not being
actioned (possible bugs or unachievable lines of code).
"""

from os import getenv
from typing import Any, Dict

import mock
import pytest
from flask.testing import FlaskClient
from flask.wrappers import Response

from services.popular_repo_app.application.app import app
from services.popular_repo_app.application.config import Config


def assert_internal_server_response(response: Response):
    """
    Check if internal server response is valid.

    Status code should be 500 and the body equals to:

    {"message": "Internal server problems, please try again later."}

    Args:
        response (Response): Response returned from the application.

    Raises:
        AssertException: When one of the validations fail.
    """
    assert response.status_code == 500
    assert response.json == {
        "message": "Internal server problems, please try again later."
    }


def assert_not_found_response(response: Response):
    """
    Check if not found response is valid.

    Status code should be 404 and the body equals to:

    {"message": "Resource not found."}

    Args:
        response (Response): Response returned from the application.

    Raises:
        AssertException: When one of the validations fail.
    """
    assert response.status_code == 404
    assert response.json == {"message": "Resource not found."}


def assert_successful_response(response: Response, should_be_popular: bool):
    """
    Check if the response is 200 and with a valid content.

    Args:
        response (Response): Response returned from the application.
        should_be_popular (bool): Defines if the response should come
            with the popular field True or False.
    Raises:
        AssertException: When a validation fails.
    """
    assert response.status_code == 200
    assert_successful_response_body(response.json, should_be_popular)


def assert_successful_response_body(
    response_body: Dict[str, Any], should_be_popular: bool
):
    """
    Check if response body is valid.

    The body must contain the keys num_forks (int), num_starts (int),
    popular (bool) and score (int).

    The popular field must be set to the value passed in the param
    should_be_popular.

    Args:
        response_body (Dict[str, Any]): Body of the response returned
            from the application.
        should_be_popular (bool): Defines if the response should come
            with the popular field True or False.

    Raises:
        AssertException: When a validation fails.
    """
    assert isinstance(response_body.get("num_forks"), int)
    assert isinstance(response_body.get("num_stars"), int)
    assert isinstance(response_body.get("score"), int)
    assert isinstance(response_body.get("popular"), bool)
    if should_be_popular:
        assert response_body["popular"]
    else:
        assert not response_body["popular"]
    assert (
        response_body["score"]
        == 2 * response_body["num_forks"] + response_body["num_stars"]
    )
    if response_body["score"] < 500:
        assert not response_body["popular"]
    else:
        assert response_body["popular"]


def assert_wrong_credentials(response: Response):
    """
    Check if response is an Unauthorized response.

    Status code should be 401 and the body equals to:

    {
        "message": "Invalid Github credentials. Set it as the
                    env var GITHUB_ACCESS_TOKEN"
    }

    Args:
        response (Response): Response returned from the application.

    Raises:
        AssertException: When one of the validations fail.
    """
    assert response.status_code == 401
    assert response.json == {
        "message": "Invalid Github credentials. Set it as the "
        "env var GITHUB_ACCESS_TOKEN"
    }


@pytest.fixture(scope="session")
def app_test_client() -> FlaskClient:
    """
    Provide a test client for the application.

    Flask framework provides an out-of-the-box testing
    object to an application.

    Returns:
        FlaskClient: Test client for the application.
    """
    with app.test_client() as client:
        yield client


def test_get_wrong_url(app_test_client: FlaskClient):
    """
    Test a get request to a URL that does not exist in the app.

    The response must be a valid 404.

    Args:
        app_test_client (FlaskClient): Test client for the application
            provided out-of-the-box by the Flask framework.
    """
    response = app_test_client.get("/")
    assert_not_found_response(response)


def test_post_to_main_endpoint(app_test_client: FlaskClient):
    """
    Test a post request to the main endpoint.

    The response must be a 405 -> Method not allowed.

    Args:
        app_test_client (FlaskClient): Test client for the application
            provided out-of-the-box by the Flask framework.
    """
    response = app_test_client.post("xxxxx/flask", json={})
    assert response.status_code == 405  # Method not allowed status.


def test_get_non_existent_user_name(app_test_client: FlaskClient):
    """
    Test getting the popularity of a repo with an invalid user name.

    A 404 response must be returned.

    Args:
        app_test_client (FlaskClient): Test client for the application
            provided out-of-the-box by the Flask framework.
    """
    response = app_test_client.get("xxxxx/flask")
    assert_not_found_response(response)


def test_get_non_existent_repo(app_test_client: FlaskClient):
    """
    Test getting the popularity of a repo that does not exist.

    A 404 response must be returned.

    Args:
        app_test_client (FlaskClient): Test client for the application
            provided out-of-the-box by the Flask framework.
    """
    response = app_test_client.get("pallets/xxxxx")
    assert_not_found_response(response)


def test_get_popular_repository(app_test_client: FlaskClient):
    """
    Test getting the popularity of a repo which is popular.

    A 200 response must be returned. The body must contain
    the keys num_forks (int), num_starts (int), popular (bool)
    and score (int).

    The popular field must be True.

    Args:
        app_test_client (FlaskClient): Test client for the application
            provided out-of-the-box by the Flask framework.
    """
    response = app_test_client.get("pallets/flask")
    assert_successful_response(response, should_be_popular=True)


def test_get_unpopular_repository(app_test_client: FlaskClient):
    """
    Test getting the popularity of a repo which is popular.

    A 200 response must be returned. The body must contain
    the keys num_forks (int), num_starts (int), popular (bool)
    and score (int).

    The popular field must be False.

    Args:
        app_test_client (FlaskClient): Test client for the application
            provided out-of-the-box by the Flask framework.
    """
    response = app_test_client.get("gabrielsm90/covid19-monitor")
    assert_successful_response(response, should_be_popular=False)


@mock.patch("requests.get")
def test_get_repo_with_github_api_down(
    mocked_get: mock.MagicMock, app_test_client: FlaskClient
):
    """
    Test the behavior of the application if connection with Github fails.

    A 500 response must be returned.

    Args:
        mocked_get (mock.MagicMock): Mocker for the get request. It will always
            throw an exception.
        app_test_client (FlaskClient): Test client for the application
            provided out-of-the-box by the Flask framework.
    """
    mocked_get.side_effect = Exception("Exception from Github")
    response = app_test_client.get("pallets/flask")
    assert_internal_server_response(response)


def test_get_repo_without_github_credentials(app_test_client: FlaskClient):
    """
    Test the behavior of the application if there is no Github access token.

    A 401 response must be returned.

    Args:
        app_test_client (FlaskClient): Test client for the application
            provided out-of-the-box by the Flask framework.
    """
    Config.GITHUB_ACCESS_TOKEN = None
    response = app_test_client.get("pallets/flask")
    Config.GITHUB_ACCESS_TOKEN = getenv("GITHUB_ACCESS_TOKEN")
    assert_wrong_credentials(response)


def test_get_repo_with_invalid_github_credentials(app_test_client: FlaskClient):
    """
    Test the behavior of the application with invalid Github access token.

    A 401 response must be returned.

    Args:
        app_test_client (FlaskClient): Test client for the application
            provided out-of-the-box by the Flask framework.
    """
    Config.GITHUB_ACCESS_TOKEN = "invalid-token"
    response = app_test_client.get("pallets/flask")
    Config.GITHUB_ACCESS_TOKEN = getenv("GITHUB_ACCESS_TOKEN")
    assert_wrong_credentials(response)


def test_get_health_endpoint(app_test_client: FlaskClient):
    """
    Test the health endpoint.

    Args:
        app_test_client (FlaskClient): Test client for the application
            provided out-of-the-box by the Flask framework.
    """
    response = app_test_client.get("health")
    assert response.status_code == 200


@mock.patch("requests.get")
def test_get_health_endpoint_with_github_down(
    mocked_get: mock.MagicMock, app_test_client: FlaskClient
):
    """
    Test the health endpoint with github down.

    Args:
        app_test_client (FlaskClient): Test client for the application
            provided out-of-the-box by the Flask framework.
    """
    mocked_get.side_effect = Exception("Exception from github connection")
    response = app_test_client.get("health")
    assert response.status_code == 500
