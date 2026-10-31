# 5. Sending data with POST

File: [`main.py`](main.py). Run: `fastapi dev main.py`

`GET` asks for data. `POST` **sends** data to the server so it can save it. The
data travels in the **body** of the request, as JSON. A browser address bar can
only do `GET`, so we test `POST` in the **`/docs`** page (topic 7).

## Describe the data

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
```

Think of this class as a **form**: it lists the fields the server expects and
their types. Put it in the function and FastAPI fills it from the JSON.

```python
# Postman: POST http://127.0.0.1:8000/items
#   Body > raw > JSON: {"name": "Notebook", "price": 2.5}
@app.post("/items")
def add_item(item: Item):
    return {"message": f"Added {item.name}", "price": item.price}
```

## Try it in /docs

1. Open `http://127.0.0.1:8000/docs`, click `POST /items`, then **Try it out**.
2. Body:

   ```json
   {"name": "Notebook", "price": 2.5}
   ```

3. **Execute**. You get `{"message":"Added Notebook","price":2.5}`.
4. Remove `price` and execute again. FastAPI refuses and tells you which field
   is missing.

## Key points

- `POST` sends data in a JSON body.
- A `BaseModel` class is the form that says what the data looks like.
- You will ask AI to write these classes for you. You only need to read them.
