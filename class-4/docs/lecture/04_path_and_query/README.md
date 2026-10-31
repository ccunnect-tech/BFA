# 4. Sending a value in the URL

File: [`main.py`](main.py). Run: `fastapi dev main.py`

The client can send a value to the server inside the URL. There are two ways.

| Name | Where it is in the URL | Example | In the code |
|------|------------------------|---------|-------------|
| **Path parameter** | after a `/`, written as `{name}` in the route | `/greet/Asha` | `@app.get("/greet/{name}")` |
| **Query parameter** | after the `?`, as `key=value` (join more with `&`) | `/ticket-price?age=20&student=true` | `age`, `student` (not in the path) |

Either way, the value arrives in your function as an **argument** with the
same name: `greet(name)` gets `"Asha"`, `ticket_price(age, student)` gets `20`
and `True`.

## In the path

```python
# Postman: GET http://127.0.0.1:8000/greet/Asha
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}
```

`/greet/Asha` gives `{"message":"Hello, Asha!"}`. The `{name}` in the path
becomes the `name` in the function.

## After the `?` (query)

```python
# Postman: GET http://127.0.0.1:8000/ticket-price?age=20&student=true
@app.get("/ticket-price")
def ticket_price(age: int, student: bool = False):
    ...
```

`/ticket-price?age=20&student=true`. A parameter that is not in the path comes
from the `?` part. `student: bool = False` has a default, so it is optional.

## The `: int` helps you

`age: int` tells FastAPI to turn the text `"20"` into the number `20`. If the
client sends `age=old`, FastAPI answers with an error message for you. You write
no checking code.

## Try it

1. Open `/greet/Asha`, then `/greet/Sam`.
2. Open `/ticket-price?age=3`, `/ticket-price?age=30`, `/ticket-price?age=30&student=true`.
3. Open `/ticket-price?age=old` and read the error.
4. Add a route `/square/{n}` that returns `n * n`.

## Key points

- A value in the path or after the `?` becomes a function parameter.
- The type (`int`, `str`, `bool`) makes FastAPI convert it.
