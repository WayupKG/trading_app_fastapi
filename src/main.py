from fastapi import FastAPI

from src.auth.base_config import auth_backend, fastapi_users
from src.auth.schemes import UserCreate, UserRead

from src.operations.routers import router as router_operation

app = FastAPI(
    title='Trading App API'
)

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
