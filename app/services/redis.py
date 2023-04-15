from uuid import uuid4

from fastapi import UploadFile

from app.configs import redis


def get_file_key() -> str:
    return redis.FILE_KEY + str(uuid4())


async def store_file(file: UploadFile) -> str:
    key = get_file_key()
    await redis.redis_client.set(key, file.file.read(), 3 * 60)
    return key
