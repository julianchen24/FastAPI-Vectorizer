from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from microservices.database import SessionDep
from .database import SessionDep
from .models import Invoice
from . import crud

router = APIRouter()

@router.post("/invoices/")
def create_invoice_endpoint(invoice: Invoice, session: SessionDep):
    return crud.create_invoice(invoice, session)

@router.get("/invoices/")
def get_invoices_endpoint(session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    return crud.read_invoices(session, offset, limit)

@router.get("/invoices/{invoice_id}")
def get_invoice_endpoint(invoice_id: int, session: SessionDep):
    return crud.read_invoice(invoice_id, session)

@router.patch("/invoices/{invoice_id}")
def update_invoice_endpoint(invoice_id: int, invoice: Invoice, session: SessionDep):
    return crud.update_invoice(invoice_id, invoice, session)

@router.delete("/invoices/{invoice_id}")
def delete_invoice_endpoint(invoice_id: int, session: SessionDep):
    return crud.delete_invoice(invoice_id, session)

@router.get("/")
def read_all_products(session: SessionDep):
    products = session.exec(select(Invoice)).all()
    return products
