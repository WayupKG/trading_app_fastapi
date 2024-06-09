from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean

from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

metadata = MetaData()

operation = Table(
    'operation',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('quantity', String),
    Column('figi', String),
    Column('instrument_type', String, nullable=True),
    Column('date', TIMESTAMP),
    Column('type', String),
)
