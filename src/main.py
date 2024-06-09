from fastapi import FastAPI

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

from src.auth.base_config import auth_backend, fastapi_users
from src.auth.schemes import UserCreate, UserRead

from src.operations.routers import router as router_operation

app = FastAPI(
    title='Trading App API'
)


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url("redis://redis")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


@app.on_event("startup")
async def startup() -> None:
    redis = aioredis.from_url("redis://redis", decode_responses=True, encoding="utf-8")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router_operation)

