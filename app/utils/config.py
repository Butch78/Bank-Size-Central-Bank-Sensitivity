from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Bank-Size-Central-Bank-Sensitivity"
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []


settings = Settings()
