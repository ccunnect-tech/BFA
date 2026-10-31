# HOW TO RUN
#   1. One time only, install FastAPI:  pip install "fastapi[standard]"
#      (Mac: pip3 install "fastapi[standard]")
#   2. Open the VS Code terminal in this file's folder and run:  fastapi dev 01_hello_api.py
#      (if "fastapi" is not found:  python -m fastapi dev 01_hello_api.py   Mac: python3 -m ...)
#   3. Open http://127.0.0.1:8000/docs   (stop the server with Ctrl + C)

# Live practice 1: Hello API
# ------------------------------------------------------------
# TOPICS: FastAPI app, @app.get, a route, JSON
#
# PROBLEM
# Build your first API with ONE route:
#   GET /   returns {"message": "Hello, API"}
#
# RUN (same on Mac and Windows)
#   fastapi dev 01_hello_api.py
# Then open http://127.0.0.1:8000/ in the browser, and also try /docs.
#
# EXPECTED OUTPUT (what the browser shows)
#   /          {"message":"Hello, API"}
#   /nothing   {"detail":"Not Found"}
# ------------------------------------------------------------
from fastapi import FastAPI

app = FastAPI()

# POSTMAN: once you write the route, call it (fastapi dev <this file> must be running):
#   GET    http://127.0.0.1:8000/
# Write your code below this line

