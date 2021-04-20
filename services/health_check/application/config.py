"""Configuration module."""

from os import getenv


class Config:
    """Class holding the configuration values required by the health checker."""

    POPULAR_REPOS_API_URL = getenv(
        "POPULAR_REPOS_API_URL", "http://localhost:5000/health"
    )
    HEALTH_CHECK_INTERVAL = 1  # minutes
