from sqlmodel import create_engine, SQLModel, Session
from typing import Annotated
from fastapi import Depends

from microservices.customer_service.models import Customer
from microservices.product_service.models import Product
from microservices.invoice_service.models import Invoice

sqlite_file_name = "shared_database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

# Function to create tables across services
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Dependency to get a session
def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
