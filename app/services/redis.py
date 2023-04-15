import base64
from uuid import uuid4

from fastapi import UploadFile

from app.configs import redis


def get_file_key() -> str:
    return redis.FILE_KEY + str(uuid4())


def get_base64_encoded(file: bytes) -> str:
    encoded = base64.b64encode(file)
    return encoded.decode()


async def store_file(file: UploadFile) -> str:
    file_data = await file.read()
    encoded = get_base64_encoded(file_data)
    key = get_file_key()
    await redis.redis_client.set(key, encoded, 3 * 60)
    return key


def get_base64_decoded(encoded_data: str) -> bytes:
    decoded = encoded_data.encode()
    return base64.b64decode(decoded)
