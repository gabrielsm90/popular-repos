from flask import Flask


def not_found_response(e):
    """Handle 404 errors."""
    return {"message": "Resource not found."}, 404


def invalid_credentials_response(e):
    """Handle 401 errors."""
    return {
        "message": "Invalid Github credentials. Set it as the env var GITHUB_ACCESS_TOKEN"
    }, 401


def internal_error_response(e):
    """Handle 401 errors."""
    return {
        "message": "Internal server problems, please try again later."
    }, 500


# Creates the Flask app.
app = Flask(__name__)
app.register_error_handler(404, not_found_response)
app.register_error_handler(401, invalid_credentials_response)
app.register_error_handler(500, internal_error_response)
