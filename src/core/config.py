from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = True
    DATABASE_URL: str = "postgresql+asyncpg://test:test@localhost/test"


settings = Settings()
