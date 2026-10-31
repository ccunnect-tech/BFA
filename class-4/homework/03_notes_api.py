# HOW TO RUN
#   1. One time only, install FastAPI:  pip install "fastapi[standard]"
#      (Mac: pip3 install "fastapi[standard]")
#   2. Open the VS Code terminal in this file's folder and run:  fastapi dev 03_notes_api.py
#      (if "fastapi" is not found:  python -m fastapi dev 03_notes_api.py   Mac: python3 -m ...)
#   3. Open http://127.0.0.1:8000/docs   (stop the server with Ctrl + C)

# Homework 3: Notes API
# ------------------------------------------------------------
# TOPICS: GET, POST, DELETE, a model class, a list in memory
# Build it like the to-do API from class (lecture/06_todo_crud/main.py).
# You may look at that file. Type the code yourself instead of copying it.
#
# PROBLEM
# Notes live in the list below. Make a model NoteIn with title (str) and
# text (str). Add three routes:
#   1. GET    /notes             returns the whole list
#   2. POST   /notes             adds a note and returns it. Give it the next id:
#                                the id of the last note + 1 (or 1 if the list
#                                is empty).
#   3. DELETE /notes/{note_id}   removes the note with that id and returns
#                                {"deleted": note_id}
#
# RUN, then test every route in http://127.0.0.1:8000/docs
#   fastapi dev 03_notes_api.py
#
# EXPECTED OUTPUT
#   GET /notes      the two notes below
#   POST /notes     {"title": "Gym", "text": "Mon and Wed"}
#                   {"id":3,"title":"Gym","text":"Mon and Wed"}
#   DELETE /notes/3 {"deleted":3}  and GET /notes shows two notes again
# ------------------------------------------------------------
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

notes = [
    {"id": 1, "title": "Shopping", "text": "Milk, eggs, bread"},
    {"id": 2, "title": "Study plan", "text": "FastAPI on Saturday"},
]

# POSTMAN: once you write the routes, call them (fastapi dev <this file> must be running):
#   GET    http://127.0.0.1:8000/notes
#   POST   http://127.0.0.1:8000/notes
#          Body > raw > JSON: {"title": "Gym", "text": "Mon and Wed"}
#   DELETE http://127.0.0.1:8000/notes/3
# Write your code below this line

