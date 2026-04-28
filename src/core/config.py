from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = True
    DATABASE_URL: str = "postgresql+asyncpg://test:test@localhost/test"

    # jwt
    jwt_secret: str = "placeholder_jwt_secret_long_enough_to_dimiss"
    jwt_algorithm: str = "HS256"
    jwt_access_token_ttl_minutes: int = 30
    jwt_refresh_token_ttl_days: int = 2
    jwt_issuer: str = "newsjall"


settings = Settings()
