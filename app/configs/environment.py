from functools import lru_cache

from pydantic import BaseSettings, RedisDsn


class Settings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: str

    @property
    def redis_uri(self) -> RedisDsn:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"


@lru_cache
def get_settings() -> Settings:
    return Settings()
