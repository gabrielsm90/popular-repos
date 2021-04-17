"""Main module which starts the application."""

from services.popular_repo_app.application.app import app


if __name__ == "__main__":
    app.run(host="0.0.0.0")  # noqa
