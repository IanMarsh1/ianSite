"""
This module defines the routes for the Flask application.

It includes routes for the home page, projects page, cool page, and contact page.
"""

from flask import render_template

def init_routes(app):
    """
    Initialize the routes for the Flask application.

    Args:
        app (Flask): The Flask application instance.
    """

    @app.route('/')
    @app.route('/index')
    def home():
        """
        Handle the home page and index routes.

        Returns:
            str: The rendered HTML template for the home page.
        """
        return render_template('index.html')

    @app.route('/projects')
    def projects():
        """
        Handle the projects page route.

        Returns:
            str: The rendered HTML template for the projects page.
        """
        return render_template('projects.html')

    @app.route('/cool')
    def cool():
        """
        Handle the cool page route.

        Returns:
            str: The rendered HTML template for the cool page.
        """
        return render_template('cool.html')

    @app.route('/contact')
    def contact():
        """
        Handle the contact page route.

        Returns:
            str: The rendered HTML template for the contact page.
        """
        return render_template('contact.html')
