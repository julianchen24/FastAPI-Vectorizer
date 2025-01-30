from typing import Annotated
from fastapi import HTTPException, Query
from sqlmodel import select
from microservices.Database import SessionDep
from models import Invoice

def create_invoice(invoice: Invoice, session: SessionDep):
    db_invoice = Invoice.model_validate(invoice)
    session.add(db_invoice)
    session.commit()
    session.refresh(db_invoice)
    return db_invoice

def read_invoices(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100
):
    invoices = session.exec(select(Invoice).offset(offset).limit(limit)).all()
    return invoices

def read_invoice(invoice_id: int, session: SessionDep):
    invoice = session.get(Invoice, invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice

def update_invoice(invoice_id: int, invoice: Invoice, session: SessionDep):
    invoice_db = session.get(Invoice, invoice_id)
    if not invoice_db:
        raise HTTPException(status_code=404, detail="Invoice not found")
    
    invoice_data = invoice.model_dump(exclude_unset=True)
    invoice_db.sqlmodel_update(invoice_data)
    session.add(invoice_db)
    session.commit()
    session.refresh(invoice_db)
    return invoice_db

def delete_invoice(invoice_id: int, session: SessionDep):
    invoice = session.get(Invoice, invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    session.delete(invoice)
    session.commit()
    return {"ok": True}
