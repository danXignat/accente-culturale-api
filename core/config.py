
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    app_name: str = "Accente-Culturale-API"

    DATABASE_URL: str 
    JWT_SECRET_KEY: str 
    ADMIN_USERNAME: str 
    ADMIN_PASSWORD: str 
    ENVIRONMENT: str = "development"
    class Config:
        env_file = ".env"
        case_sensitive = False
        extra = "allow"

settings = Settings()