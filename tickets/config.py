from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USERNAME: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    DB_NAME: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_COOKIE_KEY: str = "access_token"
    JWT_SECRET: str
    JWT_EXPIRY_DURATION_IN_WEEKS: int = 4

    class Config:
        env_file = ".env"


settings = Settings()
