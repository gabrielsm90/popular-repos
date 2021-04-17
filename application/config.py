"""Configuration module."""

from os import getenv


class Config:
    """Holds the configuration values required by the app."""

    GITHUB_ACCESS_TOKEN = getenv("GITHUB_ACCESS_TOKEN")
    GITHUB_API_URL = "https://api.github.com"
