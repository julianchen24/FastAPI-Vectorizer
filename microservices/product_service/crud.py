from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from microservices.Database import get_session

@app.post("/products/")
def create_product(product: Product, session: Session = Depends(get_session)):
    db_product = Product.model_validate()
