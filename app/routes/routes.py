from arq import ArqRedis
from fastapi import APIRouter, Depends, UploadFile

from app.dependencies import check_file_size, get_arq_redis
from app.services.redis import store_file

router = APIRouter(prefix="/data", tags=["Transformation"])


@router.post("/")
async def call_example(redis: ArqRedis = Depends(get_arq_redis)):
    await redis.enqueue_job("example")
    return {"started": True}


@router.post("/upload")
async def upload_data(file: UploadFile = Depends(check_file_size)):
    key = await store_file(file)
    return {"key": key}
