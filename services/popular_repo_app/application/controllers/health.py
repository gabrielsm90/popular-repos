"""Controller for the app's endpoint."""
from typing import Dict

from flask import Blueprint

from services.popular_repo_app.application.service.github_client import (
    check_github_api_connection,
)


health = Blueprint("health", __name__)


@health.route("/health", methods=("GET",))
def check_health() -> Dict[str, str]:
    """
    Check app health.

    Validates if connection with Github API
    is working.

    Returns:
        Dict[str, str]: OK message.

    Raises:
        HTTPError: If connection with
            github is not working.
    """
    check_github_api_connection()
    return {"message": "ok"}
