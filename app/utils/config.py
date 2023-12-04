from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Bank-Size-Central-Bank-Sensitivity"
    BACKEND_CORS_ORIGINS: list[str] = []


settings = Settings()