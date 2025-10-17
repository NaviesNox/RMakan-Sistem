""" Konfigurasi ENV """
import logging
from pydantic import BaseSettings

class Settings(BaseSettings):
    """ Class Settings untuk konfigurasi ENV """
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost:5432/mydatabase"
    PROJECT_NAME: str = "FastAPI with SQLAlchemy"
    PROJECT_VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = True

    SECRET_KEY: str = "your-secret-key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  
    ALGORITHM: str  = "HS256"


    


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

if not settings.DATABASE_URL:
    logging.warning("Variable DATABASE_URL belum di set.    Harap isi di .env untuk produksi.")

if not settings.SECRET_KEY:
    logging.warning("Variable SECRET_KEY belum di set. Harap isi di .env untuk produksi.")

