"""
Factory function to create and configure a Flask application instance.

This function initializes a Flask app using the application factory pattern,
sets up routes by importing and calling the `init_routes` function, and returns
the configured app instance.
"""

from flask import Flask
from .routes import init_routes

def create_app():
    """
        Create and configure a Flask application instance.

        Returns:
            Flask: The configured Flask application instance.
    """
    app = Flask(__name__)
    init_routes(app)

    return app
