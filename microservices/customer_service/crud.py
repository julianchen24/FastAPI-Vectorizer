from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from microservices.Database import SessionDep, get_session
from models import Customer

def create_customer(customer: Customer, session: SessionDep):
    db_customer = Customer.model_validate(customer)
    session.add(customer)
    session.commit()
    session.refresh(db_customer)
    return db_customer

def read_customers(
    session: SessionDep,
    offset:int=0,
    limit: Annotated[int,Query(le=100)]=100
):
    customers = session.exec(select(Customer).offset(offset).limit(limit)).all()
    return customers

def read_customer(customer_id:int, session: SessionDep):
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code="404",detail="Customer not found")
    return customer

def update_customer(customer_id: int, customer: Customer, session: SessionDep):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(status_code="404", detail="Customer not found")
    customer_data = customer.model_dump(exclude_unset=True)
    customer_db.sqlmodel_update(customer_data)
    session.add(customer_db)
    session.commit()
    session.refresh(customer_db)
    return customer_db

def delete_customer(customer_id: int, session: SessionDep):
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code="404", detail="Customer not found")
    session.delete(customer)
    session.commit()
    return{"ok": True}

