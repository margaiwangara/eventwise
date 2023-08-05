from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    JWT_SECRET: str
    JWT_EXPIRY_DURATION_IN_WEEKS: int = 4
    POSTGRES_USERNAME: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    DB_NAME: str

    class Config:
        env_file = ".env"


settings = Settings()
