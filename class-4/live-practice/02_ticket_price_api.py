# HOW TO RUN
#   1. One time only, install FastAPI:  pip install "fastapi[standard]"
#      (Mac: pip3 install "fastapi[standard]")
#   2. Open the VS Code terminal in this file's folder and run:  fastapi dev 02_ticket_price_api.py
#      (if "fastapi" is not found:  python -m fastapi dev 02_ticket_price_api.py   Mac: python3 -m ...)
#   3. Open http://127.0.0.1:8000/docs   (stop the server with Ctrl + C)

# Live practice 2: Ticket price API
# ------------------------------------------------------------
# TOPICS: query parameters, type hints, default values, if / elif / else
#
# PROBLEM
# This is the ticket price task from Class 2, now as an API.
# Add a route  GET /ticket-price  with two query parameters:
#   age      (int, required)
#   student  (bool, optional, default False)
# Rules, checked in this order:
#   - under 5 years old ........................ $0
#   - age 5 to 12, or age 65 and over .......... $8
#   - a student ................................ $10
#   - everyone else ............................ $12
# Return a dict with the age, student and price.
#
# RUN
#   fastapi dev 02_ticket_price_api.py
#
# EXPECTED OUTPUT (what the browser shows)
#   /ticket-price?age=20&student=true   {"age":20,"student":true,"price":10}
#   /ticket-price?age=3                 {"age":3,"student":false,"price":0}
#   /ticket-price?age=70                {"age":70,"student":false,"price":8}
#   /ticket-price                       422 error (age is required)
#   /ticket-price?age=old               422 error (age must be an integer)
# ------------------------------------------------------------
from fastapi import FastAPI

app = FastAPI()

# POSTMAN: once you write the routes, call them (fastapi dev <this file> must be running):
#   GET    http://127.0.0.1:8000/ticket-price?age=20&student=true
#   GET    http://127.0.0.1:8000/ticket-price?age=3
#   GET    http://127.0.0.1:8000/ticket-price?age=70
# Write your code below this line

