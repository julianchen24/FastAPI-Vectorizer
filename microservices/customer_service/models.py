from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from datetime import datetime

class Customer(SQLModel, table=True):
    customer_id:int | None = Field(default=None, primary_key=True)
    name:str = Field(index=True)
    phone:str 
    address:str 
    email:str = Field(index=True)