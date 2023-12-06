from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: list

    DBHOST: str
    DBUSER: str
    DBPASS: str
    DBNAME: str
    DBPORT: str
    READ_ONLY_DBUSER: str
    READ_ONLY_DBPASS: str



settings = Settings(_env_file='.env', _env_file_encoding='utf-8')
