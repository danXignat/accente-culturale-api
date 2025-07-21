
from pydantic_settings import BaseSettings
from typing import Optional

if os.getenv("ENVIRONMENT") != "production":
    from dotenv import load_dotenv
    load_dotenv()

class Settings(BaseSettings):
    app_name: str = "Accente-Culturale-API"

    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./data/db.sqlite")

    JWT_SECRET_KEY: str 
    ADMIN_USERNAME: str 
    ADMIN_PASSWORD: str 
    ENVIRONMENT: str = "development"

    port: int = int(os.getenv("PORT", 8000))

    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()