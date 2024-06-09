from datetime import datetime
from enum import Enum
from typing import Optional, List

from pydantic import BaseModel, Field

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationException
from fastapi.responses import JSONResponse


app = FastAPI(
    title="Trading App"
)


@app.exception_handler(ValidationException)
async def validation_exception_handler(request: Request, exc: ValidationException):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()})
    )


fake_users = [
    {"id": 1, "role": "admin", "name": "Adi"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt", "degree": [
        {"id": 1, "created_at": "2020-01-01T00:00:00", "type_degree": "expert"},
    ]},
]


class DegreeType(Enum):
    newbie = "newbie"
    expert = "expert"


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = []


@app.get('/users/{user_id}', response_model=List[User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]


fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 3, "currency": "ECT", "side": "sell", "price": 43, "amount": 2.11},
    {"id": 3, "user_id": 2, "currency": "BTC", "side": "buy", "price": 323, "amount": 2.14},
    {"id": 4, "user_id": 1, "currency": "BTC", "side": "sell", "price": 543, "amount": 2.16},
]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str
    price: float = Field(ge=0)
    amount: float


@app.post("/trades")
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {"status": 201, "data": fake_trades}
