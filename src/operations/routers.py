import time
from typing import List

from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.operations.models import operation
from src.operations.schemas import OperationCreate, OperationRead

from src.tasks.tasks import add

router = APIRouter(
    prefix="/operations",
    tags=["Operations"],
)


@router.get("/", response_model=List[OperationRead])
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.type == operation_type)
    result = await session.execute(query)
    return result.all()


@router.post("/")
async def add_specific_operation(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    result = await session.execute(stmt)
    await session.commit()
    return {'success': result}


@router.get("/test-redis-cache/")
@cache(expire=30)
async def index():
    time.sleep(5)
    add.delay(1, 2)
    return dict(hello="world")


