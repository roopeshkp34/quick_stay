

from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    CLERK_ISSUER: str
    CLERK_JWKS_URL: str
    CLERK_SECRET_KEY: SecretStr


    class Config:
        env_file = ".env"

settings = Settings()