"""Module with the exceptions risen by the service."""


class RepositoryNotFound(Exception):
    """Repository requested was not found in Github."""

    def __init__(self):
        super(RepositoryNotFound, self).__init__()


class InvalidGithubCredentials(Exception):
    """Credentials provided to access Github API are invalid."""

    def __init__(self):
        super(InvalidGithubCredentials, self).__init__()
