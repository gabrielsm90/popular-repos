"""Controller for the app's endpoint."""

from flask import Blueprint

from services.popular_repo_app.application.service.github_client import check_github_api_connection


health = Blueprint("health", __name__)


@health.route("/health", methods=("GET",))
def check_health():
    check_github_api_connection()
    return {"message": "ok"}
