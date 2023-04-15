import io
from logging import getLogger

from redis import asyncio as aioredis

from app.services.redis import get_base64_decoded

log = getLogger(__name__)


async def read_file(ctx, key: str):
    redis: aioredis.Redis = ctx["redis_client"]
    encoded_data = await redis.get(key)
    decoded_data = get_base64_decoded(encoded_data)
    _ = io.BytesIO(decoded_data)
