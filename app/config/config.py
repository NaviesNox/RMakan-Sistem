""" Konfigurasi ENV """
from pydantic import BaseSettings

class Settings(BaseSettings):
    """ Class Settings untuk konfigurasi ENV """
    DATABASE_URL: str 
    PROJECT_NAME: str = "FastAPI with SQLAlchemy"
    PROJECT_VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = True

    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  
    ALGORITHM: str 


    


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()