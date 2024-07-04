"""Default configuration

Use env var to override
"""
import os

# isacc app variables
TORCH_MODEL_PATH = os.getenv("TORCH_MODEL_PATH")

# URL scheme to use outside of request context
# do not configure as https unless reverse proxy secured
PREFERRED_URL_SCHEME = os.getenv("PREFERRED_URL_SCHEME", 'http')

# server configs
SERVER_NAME = os.getenv("SERVER_NAME")
SECRET_KEY = os.getenv("SECRET_KEY")