from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from microservices.Database import SessionDep
from models import Product 
import crud  

router = APIRouter()

@router.post("/products/")
def create_product_endpoint(product: Product, session: SessionDep):
    return crud.create_product(session, product)

@router.get("/products/")
def get_products_endpoint(session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    return crud.read_products(session, offset, limit)

@router.get("/products/{product_id}")
def get_product_endpoint(product_id: int, session: SessionDep):
    return crud.read_product(product_id, session)

@router.patch("/products/{product_id}")
def update_product_endpoint(product_id: int, product: Product, session: SessionDep):
    return crud.update_product(product_id, product, session)

@router.delete("/products/{product_id}")
def delete_product_endpoint(product_id: int, session: SessionDep):
    return crud.delete_product(product_id, session)
