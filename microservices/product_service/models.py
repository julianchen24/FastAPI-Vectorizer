from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from datetime import datetime

class Product(SQLModel, table=True):
    product_id:int | None = Field(default=None, primary_key=True)
    name:str = Field(index=True)
    unit_price:float = Field(index=True)
    description:str | None = Field(default=None)