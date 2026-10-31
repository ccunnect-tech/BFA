# HOW TO RUN
#   1. One time only, install FastAPI:  pip install "fastapi[standard]"
#      (Mac: pip3 install "fastapi[standard]")
#   2. Open the VS Code terminal in this file's folder and run:  fastapi dev main.py
#      (if "fastapi" is not found:  python -m fastapi dev main.py   Mac: python3 -m ...)
#   3. Open http://127.0.0.1:8000/docs   (stop the server with Ctrl + C)

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


# Postman: POST http://127.0.0.1:8000/items
#   Body > raw > JSON: {"name": "Notebook", "price": 2.5}
@app.post("/items")
def add_item(item: Item):
    return {"message": f"Added {item.name}", "price": item.price}
