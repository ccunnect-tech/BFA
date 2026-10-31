# 3. Your first API

File: [`main.py`](main.py). Run it from this folder:

```
fastapi dev main.py
```

Then open these in the browser:

| URL | You see |
|-----|---------|
| `http://127.0.0.1:8000/` | `{"message":"Hello from my first API"}` |
| `http://127.0.0.1:8000/about` | `{"course":"BFA","class":4,"topic":"Backend with FastAPI"}` |
| `http://127.0.0.1:8000/nope` | `{"detail":"Not Found"}` (a 404) |

## The three parts

```python
from fastapi import FastAPI

app = FastAPI()            # 1. make the app

@app.get("/")              # 2. decorator: "GET requests to / go to the function below"
def home():                # 3. the function runs, and what it returns becomes JSON
    return {"message": "Hello from my first API"}
```

- `@app.get("/about")` is the **route**: method `GET` + path `/about`.
- Return a `dict` (or a list) and FastAPI turns it into JSON.
- Save the file and the server reloads. Refresh the browser.

Open DevTools, Network tab, then refresh. You will see the same Method and
Status columns from Class 3, now for *your* server.

## Key points

- One function per route.
- The decorator says which method and path.
- The return value is the response.
