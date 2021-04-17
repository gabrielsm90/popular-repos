from os import getenv


class Config:

    GITHUB_ACCESS_TOKEN = getenv("GITHUB_ACCESS_TOKEN")
    GITHUB_API_REPOS_URL = "https://api.github.com/repos"
