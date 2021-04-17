"""Module to interact with the Github API."""

from typing import Any, Dict

import requests

from services.popular_repo_app.application.config import Config


def check_github_api_connection():
    """
    Check if connection with Github API is working.

    Raises:
        requests.exceptions.HTTPError: If connection has
            a problem.
    """
    headers = {"Authorization": f"Bearer {Config.GITHUB_ACCESS_TOKEN}"}
    response = requests.get(Config.GITHUB_API_URL, headers=headers)
    response.raise_for_status()


def get_repository(user_name: str, repository_name: str) -> Dict[str, Any]:
    """
    Get the given repository from Github API.

    Args:
        user_name (str): Repository's owner's username.
        repository_name (str): Repository's name.

    Returns:
        Dict[str, Any]: Dictionary with all the information
            about the given repository.

    Raises:
        requests.exceptions.HTTPError: If repo wasn't found or if
            credentials are not valid.
    """
    repository_url = f"{Config.GITHUB_API_URL}/repos/{user_name}/{repository_name}"
    headers = {"Authorization": f"Bearer {Config.GITHUB_ACCESS_TOKEN}"}
    response = requests.get(repository_url, headers=headers)
    response.raise_for_status()
    return response.json()
