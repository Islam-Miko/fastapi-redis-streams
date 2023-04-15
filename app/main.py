from fastapi import FastAPI
from redis import asyncio as aioredis

from app.configs import redis
from app.configs.environment import get_settings
from app.routes.routes import router

settings = get_settings()

app = FastAPI(
    description="FastAPI example app of using ARQ, RedisStreams, Websockets"
)


@app.get("/")
async def ping():
    return {"message": "pong"}


@app.on_event("startup")
async def startup() -> None:
    pool = aioredis.ConnectionPool.from_url(
        settings.redis_uri, max_connections=10, decode_responses=True
    )
    redis.redis_client = aioredis.Redis(connection_pool=pool)


@app.on_event("shutdown")
async def shutdown() -> None:
    await redis.redis_client.close()


app.include_router(router, prefix="/api/v1")
