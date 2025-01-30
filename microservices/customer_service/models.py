from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from datetime import datetime
from .database import SessionDep

class Customer(SQLModel, table=True):
    customer_id:int | None = Field(default=None, primary_key=True)
    name:str 
    phone:str 
    address:str 
    email:str 