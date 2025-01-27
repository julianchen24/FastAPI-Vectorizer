# .\.venv\Scripts\Activate.ps1  (In powershell)
# fastapi dev main.py (In powershell)

# For some reason, not recognizing backslash
# GET: curl http://127.0.0.1:8000/items/1
# POST (NOT WORKING): curl.exe -X POST -H "Content-Type: application/json" -d "{\"name\": \"Book\", \"price\": 9.99, \"is_offer\": true}" http://127.0.0.1:8000/items/1
# PUT: curl.exe -X PUT -H "Content-Type: application/json" -d "{\"name\": \"Updated Book\", \"price\": 14.99, \"is_offer\": false}" http://127.0.0.1:8000/items/1
# DELETE: curl.exe -X DELETE http://127.0.0.1:8000/items/1

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Is this how it works?
items = {}

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in items:
        return {"error": "Item already exists"}
    items[item_id] = item
    return {"message": "Item created successfully", "item": items[item_id]}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        return {"error": "Item not found"}
    del items[item_id]
    return {"message": f"Item {item_id} deleted successfully"}
