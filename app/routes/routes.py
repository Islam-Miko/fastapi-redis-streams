from arq import ArqRedis
from fastapi import APIRouter, Depends, UploadFile

from app.dependencies import get_redis

router = APIRouter(prefix="/data", tags=["Transformation"])


@router.post("/")
async def call_example(redis: ArqRedis = Depends(get_redis)):
    await redis.enqueue_job("example")
    return {"started": True}


@router.post("/upload")
async def upload_data(file: UploadFile):
    return {"filename": file.filename}
