from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, TIMESTAMP


class OperationRead(BaseModel):
    id: int
    quantity: str
    figi: str
    instrument_type: str
    date: datetime
    type: str


class OperationCreate(BaseModel):
    id: int
    quantity: str
    figi: str
    instrument_type: str
    date: datetime
    type: str

