import datetime

from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    registered_at: datetime.datetime
    role_id: Optional[int]
    is_active: bool
    is_superuser: bool
    is_verified: bool


class UserCreate(schemas.BaseUserCreate):
    id: int
    email: str
    username: str
    password: str
    role_id: Optional[int]
    is_active: bool
    is_superuser: bool
    is_verified: bool

