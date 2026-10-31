# HOW TO RUN
#   1. One time only, install FastAPI:  pip install "fastapi[standard]"
#      (Mac: pip3 install "fastapi[standard]")
#   2. Open the VS Code terminal in this file's folder and run:  fastapi dev 03_books_api.py
#      (if "fastapi" is not found:  python -m fastapi dev 03_books_api.py   Mac: python3 -m ...)
#   3. Open http://127.0.0.1:8000/docs   (stop the server with Ctrl + C)

# Live practice 3: Books API
# ------------------------------------------------------------
# TOPICS: GET, POST, a model class (the "form"), a list in memory
#
# PROBLEM
# Keep a list of books in memory (the list below). Add two routes:
#   1. GET  /books    returns the whole list
#   2. POST /books    adds a book. The body is {"title": ..., "author": ...}
#                     Make a model class BookIn for the body (like NewTask in
#                     the lecture). Give the new book the next id
#                     (len(books) + 1), add it to the list, and return it.
#
# RUN, then test both routes in http://127.0.0.1:8000/docs
#   fastapi dev 03_books_api.py
#
# EXPECTED OUTPUT
#   GET /books    [{"id":1,"title":"Dune","author":"Frank Herbert"}, ...]
#   POST /books  with  {"title": "Emma", "author": "Jane Austen"}
#                 {"id":3,"title":"Emma","author":"Jane Austen"}
#   GET /books    now shows 3 books
# ------------------------------------------------------------
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

books = [
    {"id": 1, "title": "Dune", "author": "Frank Herbert"},
    {"id": 2, "title": "Matilda", "author": "Roald Dahl"},
]

# POSTMAN: once you write the routes, call them (fastapi dev <this file> must be running):
#   GET    http://127.0.0.1:8000/books
#   POST   http://127.0.0.1:8000/books
#          Body > raw > JSON: {"title": "Emma", "author": "Jane Austen"}
# Write your code below this line

