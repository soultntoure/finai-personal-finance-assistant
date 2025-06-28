import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List, Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "FinAI Backend MVP"
    API_V1_STR: str = "/api/v1"

    DATABASE_URL: str
    BACKEND_SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 # 7 days

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000"]

    # Plaid
    BACKEND_PLAID_ENV: str = "sandbox" # sandbox, development, production
    BACKEND_PLAID_CLIENT_ID: str
    BACKEND_PLAID_SECRET: str

    # ML Service
    BACKEND_ML_SERVICE_URL: str = "http://ml_service:8001"

    # Celery/Redis
    REDIS_URL: str = "redis://redis:6379/0"
    CELERY_BROKER_URL: str = "redis://redis:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://redis:6379/0"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
