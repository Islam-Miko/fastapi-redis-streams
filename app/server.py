from fastapi import FastAPI

from app.routes.routes import router

app = FastAPI(
    description="FastAPI example app of using ARQ, RedisStreams, Websockets"
)

app.include_router(router, prefix="/api/v1")


@app.get("/")
async def ping():
    return {"message": "pong"}
