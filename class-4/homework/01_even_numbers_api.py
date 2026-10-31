# HOW TO RUN
#   1. One time only, install FastAPI:  pip install "fastapi[standard]"
#      (Mac: pip3 install "fastapi[standard]")
#   2. Open the VS Code terminal in this file's folder and run:  fastapi dev 01_even_numbers_api.py
#      (if "fastapi" is not found:  python -m fastapi dev 01_even_numbers_api.py   Mac: python3 -m ...)
#   3. Open http://127.0.0.1:8000/docs   (stop the server with Ctrl + C)

# Homework 1: Even numbers API
# ------------------------------------------------------------
# TOPICS: path parameters, functions, loops, lists, JSON
# This is the even numbers task from Class 2, now as an API.
#
# PROBLEM
# Add two routes:
#   1. GET /is-even/{n}      returns {"n": n, "even": true or false}
#   2. GET /evens/{limit}    returns {"limit": limit, "evens": [..]} with every
#                            even number from 1 up to limit, in a list.
# Write a function is_even(n) and use it in both routes.
# Both parameters are ints, so /is-even/abc must give a 422 error by itself.
#
# RUN
#   fastapi dev 01_even_numbers_api.py
#
# EXPECTED OUTPUT
#   /is-even/4         {"n":4,"even":true}
#   /is-even/7         {"n":7,"even":false}
#   /evens/10          {"limit":10,"evens":[2,4,6,8,10]}
#   /evens/1           {"limit":1,"evens":[]}
#   /is-even/abc       422 error
# ------------------------------------------------------------
from fastapi import FastAPI

app = FastAPI()

# POSTMAN: once you write the routes, call them (fastapi dev <this file> must be running):
#   GET    http://127.0.0.1:8000/is-even/4
#   GET    http://127.0.0.1:8000/evens/10
# Write your code below this line

