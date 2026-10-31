# 6. A to-do API

Files: [`main.py`](main.py) and [`tasks.json`](tasks.json). Run from this folder:
`fastapi dev main.py`, then open `/docs`.

We keep the tasks in a **file**, `tasks.json`. It is a tiny database: the data
stays there when you stop the server. (A real app uses a proper database, later
in the course.)

| Request | What it does |
|---------|--------------|
| `GET /tasks` | read `tasks.json` and send the tasks |
| `POST /tasks` | add a task, then save the file |
| `DELETE /tasks/{task_id}` | remove a task, then save the file |

Together, list + add + delete (+ change) are called **CRUD**: Create, Read,
Update, Delete. Almost every app is CRUD on some kind of thing: tasks, notes,
products, users.

## How it works

Two small helper functions do all the file work:

```python
def load_tasks():              # file -> Python list
    with open(FILE) as f:
        return json.load(f)

def save_tasks(tasks):         # Python list -> file
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)
```

Every route does the same three steps: **load** the list, **change** it,
**save** it. (`GET` only loads.)

## Try it

Put `tasks.json` and `/docs` side by side on your screen.

1. `GET /tasks`: two tasks, the same as in the file.
2. `POST /tasks` with `{"title": "Learn FastAPI"}`. Look at `tasks.json`: a new
   task was written into the file.
3. `DELETE /tasks/3`. Look at the file again: it is gone.
4. Stop the server (`Ctrl + C`), start it again, `GET /tasks`: your data is
   still there. A Python list would have been empty.

To start over, put the two original tasks back in `tasks.json`.

> Run the server from inside this folder, so it can find `tasks.json`.

## The same API with a variable

The folder [`in_memory`](in_memory) has the same API where the tasks live in a
variable instead of the file. Run both and compare. Live practice 3 uses the
variable approach.

## Key points

- One kind of thing (`tasks`), three requests: list, add, delete.
- Load, change, save: the pattern behind every API that stores data.
- A JSON file keeps data after a restart. A database does the same, better.
