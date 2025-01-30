from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from microservices.Database import SessionDep, get_session
from models import Product

def create_product(product: Product, session: SessionDep):
    db_product = Product.model_validate(product)
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product

def read_products(
    session: SessionDep,
    offset:int=0,
    limit: Annotated[int,Query(le=100)]=100
):
    products = session.exec(select(Product).offset(offset).limit(limit)).all()
    return products

def read_product(product_id:int, session: SessionDep):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code="404",detail="Product not found")
    return product

def update_product(product_id: int, product: Product, session: SessionDep):
    product_db = session.get(Product, product_id)
    if not product_db:
        raise HTTPException(status_code="404", detail="Product not found")
    product_data = product.model_dump(exclude_unset=True)
    product_db.sqlmodel_update(product_data)
    session.add(product_db)
    session.commit()
    session.refresh(product_db)
    return product_db

def delete_product(product_id: int, session: SessionDep):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code="404", detail="Product not found")
    session.delete(product)
    session.commit()
    return{"ok": True}

