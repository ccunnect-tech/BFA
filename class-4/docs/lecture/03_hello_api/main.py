# HOW TO RUN
#   1. One time only, install FastAPI:  pip install "fastapi[standard]"
#      (Mac: pip3 install "fastapi[standard]")
#   2. Open the VS Code terminal in this file's folder and run:  fastapi dev main.py
#      (if "fastapi" is not found:  python -m fastapi dev main.py   Mac: python3 -m ...)
#   3. Open http://127.0.0.1:8000/docs   (stop the server with Ctrl + C)

from fastapi import FastAPI

app = FastAPI()


# Postman: GET http://127.0.0.1:8000/
@app.get("/")
def home():
    return {"message": "Hello from my first API"}


# Postman: GET http://127.0.0.1:8000/about
@app.get("/about")
def about():
    return {"course": "BFA", "class": 4, "topic": "Backend with FastAPI"}
