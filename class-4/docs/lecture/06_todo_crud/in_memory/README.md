# 6b. The same API with a variable

File: [`main.py`](main.py). Run from this folder: `fastapi dev main.py`

This is the **same to-do API** as the parent folder, but the tasks live in a
**variable** (a Python list) instead of the `tasks.json` file.

| | File (`../main.py`) | Variable (this folder) |
|---|---|---|
| Where the tasks are | `tasks.json` | the `tasks` list in the code |
| Each route | load, change, **save** | change the list |
| Stop and start the server | tasks are still there | tasks reset to the two at the top |
| Extra code | `load_tasks()` and `save_tasks()` | none |

## Try it

1. `POST /tasks` with `{"title": "Learn FastAPI"}`, then `GET /tasks`: 3 tasks.
2. Stop the server (`Ctrl + C`), start it again, `GET /tasks`: back to 2 tasks.
   Do the same in the parent folder and compare.

## Why we show both

- The variable is the simplest way to start. We use it in **Live practice 3**
  (the books API), and you will use it again in the Homework.
- A file keeps data after a restart. A real database does that and more, later
  in the course.

Same API, same routes. Only **where the data is kept** changes.
