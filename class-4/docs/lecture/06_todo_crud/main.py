# HOW TO RUN
#   1. One time only, install FastAPI:  pip install "fastapi[standard]"
#      (Mac: pip3 install "fastapi[standard]")
#   2. Open the VS Code terminal in this file's folder and run:  fastapi dev main.py
#      (if "fastapi" is not found:  python -m fastapi dev main.py   Mac: python3 -m ...)
#   3. Open http://127.0.0.1:8000/docs   (stop the server with Ctrl + C)
#   Run it from this folder, so the server can find tasks.json.

import json

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

FILE = "tasks.json"


class NewTask(BaseModel):
    title: str


def load_tasks():
    with open(FILE) as f:
        return json.load(f)


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)


# Postman: GET http://127.0.0.1:8000/tasks
@app.get("/tasks")
def list_tasks():
    return load_tasks()


# Postman: POST http://127.0.0.1:8000/tasks
#   Body > raw > JSON: {"title": "Learn FastAPI"}
@app.post("/tasks")
def add_task(body: NewTask):
    tasks = load_tasks()
    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = tasks[-1]["id"] + 1
    task = {"id": new_id, "title": body.title, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    return task


# Postman: DELETE http://127.0.0.1:8000/tasks/3
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            break
    save_tasks(tasks)
    return {"deleted": task_id}
