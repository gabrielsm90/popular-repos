import logging
import requests

from services.health_check.application.config import Config


def check_popular_repo_app_health():
    """Check if Popular Repositories App is healthy."""
    response = requests.get(Config.POPULAR_REPOS_API_URL)
    if response.status_code == 200:
        logging.info("Application healthy.")
    else:
        logging.error(f"Application with problems: {response.text}")
