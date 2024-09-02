"""
This module initializes and runs the Flask application.
It imports the create_app function from the app package, 
creates an application instance, and runs the app in debug mode.
"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
