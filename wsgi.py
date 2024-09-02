"""
This module serves as the entry point for the Flask application.
It imports the `create_app` function from the `app` package, creates an app instance,
and runs the application when executed as the main program.
"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
