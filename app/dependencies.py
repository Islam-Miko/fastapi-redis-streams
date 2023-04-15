from arq import ArqRedis, create_pool
from arq.connections import RedisSettings
from fastapi import UploadFile

from app.configs.environment import get_settings
from app.exceptions import FileTooLarge

settings = get_settings()
redis_settings = RedisSettings(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT
)


async def get_arq_redis() -> ArqRedis:
    return await create_pool(redis_settings)


async def check_file_size(file: UploadFile) -> UploadFile:
    if file.size > (5 * 10**6):
        raise FileTooLarge()
    return file
