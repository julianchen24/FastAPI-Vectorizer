# models.py
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from datetime import datetime
from .database import SessionDep

class Invoice(SQLModel, table=True):
    invoice_id:int | None = Field(default=None, primary_key=True)
    # b/c table names are automatically converted to lowercase
    customer_id:int 
    product_id:int 
    units:int 
    amount:float = Field(index=True)
    # should i make this a string or actual time
    invoice_date:str = Field(index=True)