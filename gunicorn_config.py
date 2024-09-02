"""
Gunicorn configuration for the Flask application.

This module sets up the configuration for Gunicorn, specifying:
- The bind address and port for the server
- The number of worker processes to handle requests
"""

BIND = "0.0.0.0:8000"
WORKERS = 2
