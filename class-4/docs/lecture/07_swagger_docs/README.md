# 7. The free /docs page

File: [`main.py`](main.py). Run from this folder: `fastapi dev main.py`

FastAPI reads your code and builds a web page where you can **try every route**.
No extra code. With the server running, open:

| URL | What |
|-----|------|
| `http://127.0.0.1:8000/docs` | Interactive docs (Swagger): click, fill in, run |
| `http://127.0.0.1:8000/redoc` | The same docs, read-only |

The `title` and `description` in `FastAPI(...)` are what you see at the top of
the page. The routes below them come from the `@app.get`, `@app.post` and
`@app.delete` lines.

## How to use /docs

1. Click a route to open it (for example `GET /tasks`).
2. Click **Try it out**.
3. Fill in the value or the JSON body.
4. Click **Execute**.
5. Read the **Response body** and the status code (200, 404...).

## Why it matters

- It is your test tool. You can check a route before any web page exists.
- When AI writes a route for you, `/docs` is the fastest way to see if it works.

## Try it

1. Run `main.py` and open `/docs`. Run every route once.
2. `POST /tasks` with `{"title": "Learn FastAPI"}`, then `GET /tasks`.
3. Send a bad body to `POST /tasks` (leave out `title`). Read the error.
4. Add a new route to `main.py`, save, refresh `/docs`: it appears by itself.
