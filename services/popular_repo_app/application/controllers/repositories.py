"""Controller for the app's endpoint."""

from flask import Blueprint, abort

from services.popular_repo_app.application.service.exceptions import RepositoryNotFound, InvalidGithubCredentials
from services.popular_repo_app.application.service.evaluator import get_repository_popularity


repositories = Blueprint("repositories", __name__)


@repositories.route("/<user_name>/<repository_name>", methods=("GET",))
def get_repository_classification(user_name: str, repository_name: str):
    """
    Get the repository's classification (popular or not).

    Fetches the repository from Github, calculates if it's
    popular or not and return the classification along with
    the info used to calculate it.

    Args:
        user_name (str): Repository's owner's username.
        repository_name (str): Repository's name.

    Returns:
        Dict[str, Union[int, bool]: a dictionary with the
            number of stars, number of forks, score
            and a boolean defining if the repo is
            popular or not.
    Raises:
        HTTPException: If repository not found, no credentials
            provided or an internal error. According to the
            status code, the proper error handler will be
            triggered.
    """
    try:
        return get_repository_popularity(user_name, repository_name)
    except RepositoryNotFound:
        abort(404)
    except InvalidGithubCredentials:
        abort(401)
    except Exception:
        abort(500)
