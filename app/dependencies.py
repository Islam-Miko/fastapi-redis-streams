from arq import ArqRedis, create_pool
from arq.connections import RedisSettings

from app.configs.environment import get_settings

settings = get_settings()
redis_settings = RedisSettings(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT
)


async def get_redis() -> ArqRedis:
    return await create_pool(redis_settings)
