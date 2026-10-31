# HOW TO RUN
#   1. One time only, install FastAPI:  pip install "fastapi[standard]"
#      (Mac: pip3 install "fastapi[standard]")
#   2. Open the VS Code terminal in this file's folder and run:  fastapi dev main.py
#      (if "fastapi" is not found:  python -m fastapi dev main.py   Mac: python3 -m ...)
#   3. Open http://127.0.0.1:8000/docs   (stop the server with Ctrl + C)

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# The tasks live in a variable (a list). Compare with ../main.py, which keeps
# them in tasks.json. A variable is lost when the server restarts.
tasks = [
    {"id": 1, "title": "Install Python", "done": True},
    {"id": 2, "title": "Build my first API", "done": False},
]


class NewTask(BaseModel):
    title: str


# Postman: GET http://127.0.0.1:8000/tasks
@app.get("/tasks")
def list_tasks():
    return tasks


# Postman: POST http://127.0.0.1:8000/tasks
#   Body > raw > JSON: {"title": "Learn FastAPI"}
@app.post("/tasks")
def add_task(body: NewTask):
    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = tasks[-1]["id"] + 1
    task = {"id": new_id, "title": body.title, "done": False}
    tasks.append(task)
    return task


# Postman: DELETE http://127.0.0.1:8000/tasks/3
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            break
    return {"deleted": task_id}
