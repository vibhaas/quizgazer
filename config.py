from __future__ import annotations
from dotenv import load_dotenv
import os

load_dotenv()

def _get_env(name: str, *, default: str | None = None) -> str:
    value = os.getenv(name, default)
    if value is None or not value.strip():
        raise RuntimeError(
            f"Missing required environment variable '{name}'. "
            "Set it before starting the Flask app."
        )
    return value

class Config:
    SECRET_KEY = _get_env("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = _get_env("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = os.getenv("FLASK_DEBUG", "0") == "1"
