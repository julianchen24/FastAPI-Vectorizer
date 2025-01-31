from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from .database import SessionDep
from .models import Customer


from sqlmodel import select

from . import crud

from fastapi import APIRouter

router = APIRouter() 

@router.post("/customers/")
def create_customer_endpoint(customer: Customer, session: SessionDep):
    return crud.create_customer(customer,session)

@router.get("/customers/")
def create_customers_endpoint(session:SessionDep,offset:int = 0, limit: Annotated[int,Query(le=100)] = 100):
    return crud.read_customers(session,offset,limit)

@router.get("/customers/{customer_id}")
def read_customer_endpoint(customer_id:int, session:SessionDep):
    return crud.read_customer(customer_id,session)

@router.patch("/customers/{customer_id}")
def update_customer_endpoint(customer_id:int, customer:Customer,session:SessionDep):
    return crud.update_customer(customer_id,customer,session)
    
@router.delete("/customers/{customer_id}")
def delete_customer_endpoint(customer_id:int, session:SessionDep):
    return crud.delete_customer(customer_id,session)

# ???
@router.get("/")
def read_all_products(session: SessionDep):
    products = session.exec(select(Customer)).all()
    return products


