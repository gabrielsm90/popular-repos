"""Module responsible to calculate if repository is popular or not."""

from typing import Dict, Union

from requests.exceptions import HTTPError

from services.popular_repo_app.application.service.exceptions import RepositoryNotFound, InvalidGithubCredentials
from services.popular_repo_app.application.service.github_client import get_repository


def calculate_score(num_stars: int, num_forks: int):
    """
    Calculate repo score based in the number of stars and forks.

    The formula for the score is:

    score = num_stars * 1 + num_forks * 2

    Args:
        num_stars (int): Number of stars in the repo.
        num_forks (int): Number of forks in the repo.

    Returns:
        int: Repo's score.
    """
    return num_stars + num_forks * 2


def get_repository_popularity(
    user_name: str, repository_name: str
) -> Dict[str, Union[int, bool]]:
    """
    Get the repository's popularity.

    The popularity is a dictionary with the number of stars,
    number of forks, score and a boolean defining if the repo
    is popular or not.

    Args:
        user_name (str): Repository's owner's username.
        repository_name (str): Repository's name.

    Returns:
        Dict[str, Union[int, bool]: a dictionary with the
            number of stars, number of forks, score
            and a boolean defining if the repo is
            popular or not.

    Raises:
        InvalidGithubCredentials: If call to Github returns
            a 401 error.
        RepositoryNotFound: If call to Github returns a 404.
    """
    try:
        repository = get_repository(user_name, repository_name)
    except HTTPError as e:
        if e.response.status_code == 401:
            raise InvalidGithubCredentials()
        if e.response.status_code == 404:
            raise RepositoryNotFound()
    else:
        num_stars = repository["stargazers_count"]
        num_forks = repository["forks_count"]
        score = calculate_score(num_stars, num_forks)
        return {
            "num_stars": num_stars,
            "num_forks": num_forks,
            "score": score,
            "popular": score >= 500,
        }
