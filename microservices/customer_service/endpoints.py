from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from microservices.Database import SessionDep
from models import Customer
import crud

from fastapi import APIRouter

router = APIRouter() 

@router.post("/customers/")
def create_product(customer: Customer, session: SessionDep):
    return crud.create_customer(session,customer)

@router.get("/customers/")
def read_customers(session:SessionDep,offset:int = 0, limit: Annotated[int,Query(le=100)] = 100):
    return crud.read_customers(session,offset,limit)

@router.get("/customers/{customer_id}")
def read_customer(customer_id:int, session:SessionDep):
    return crud.read_customer(customer_id,session)

@router.patch("/customers/{customer_id}")
def update_customer(customer_id:int, customer:Customer,session:SessionDep):
    return crud.update_customer(customer_id,customer,session)
    
@router.delete("/customers/{customer_id}")
def delete_customer(customer_id:int, session:SessionDep):
    return crud.delete_customer(customer_id,session)
