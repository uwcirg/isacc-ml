"""Default configuration

Use env var to override
"""
import os

# isacc app variables
TORCH_MODEL_PATH = os.getenv("TORCH_MODEL_PATH")

# server configs
SERVER_NAME = os.getenv("SERVER_NAME")
SECRET_KEY = os.getenv("SECRET_KEY")