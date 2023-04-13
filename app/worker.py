from arq import cron
from arq.connections import RedisSettings

from app.configs.environment import get_settings

settings = get_settings()


async def worker_task(ctx) -> None:
    print("This task does nothing!")


async def example(ctx):
    for _ in range(1, 10):
        print("Schwabia" * _)


class WorkerSettings:
    cron_jobs = [
        cron(
            worker_task,
            minute=10,
        )
    ]
    functions = [example]
    redis_settings = RedisSettings(
        host=settings.REDIS_HOST, port=settings.REDIS_PORT
    )
