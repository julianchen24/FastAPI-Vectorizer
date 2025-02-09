# main.py

from fastapi import FastAPI
from .endpoints import router
from pydantic import BaseModel 
from .database import SessionDep, create_db_and_tables


app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

from .endpoints import router
app.include_router(router)