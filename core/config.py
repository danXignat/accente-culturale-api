
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    app_name: str = "Accente-Culturale-API"

    database_url: str = "sqlite:///./data/db.sqlite"
    
    JWT_SECRET_KEY: str = "7d9ae0481a5018ca14ba532b84de373a"

    ADMIN_USERNAME: str = "danignat"
    ADMIN_PASSWORD: str = "$2b$12$EMScNo5n3PCCrA0jpzEBJOypJ/7KuQ7aT/QvoJG8m8a4NI2mAvY/u"

    class Config:
        env_file = ".env"

settings = Settings()