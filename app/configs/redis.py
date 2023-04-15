from typing import Final

from redis import asyncio as aioredis

redis_client: aioredis.Redis = None  # type: ignore

FILE_KEY: Final[str] = "file:"
