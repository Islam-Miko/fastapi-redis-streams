from arq import cron
from arq.connections import RedisSettings
from redis import asyncio as aioredis

from app.configs.environment import get_settings
from app.tasks import read_file

settings = get_settings()


async def worker_task(ctx) -> None:
    print("This task does nothing!")


async def startup(ctx) -> None:
    pool = aioredis.ConnectionPool.from_url(
        settings.redis_uri, max_connections=10, decode_responses=True
    )
    ctx["redis_client"] = aioredis.Redis(connection_pool=pool)


async def shutdown(ctx) -> None:
    await ctx["redis_client"].close()


class WorkerSettings:
    cron_jobs = [
        cron(
            worker_task,
            minute=10,
        )
    ]
    functions = [read_file]
    redis_settings = RedisSettings(
        host=settings.REDIS_HOST, port=settings.REDIS_PORT
    )
    on_startup = startup
    on_shutdown = shutdown
