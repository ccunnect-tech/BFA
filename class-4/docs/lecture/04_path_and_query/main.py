# HOW TO RUN
#   1. One time only, install FastAPI:  pip install "fastapi[standard]"
#      (Mac: pip3 install "fastapi[standard]")
#   2. Open the VS Code terminal in this file's folder and run:  fastapi dev main.py
#      (if "fastapi" is not found:  python -m fastapi dev main.py   Mac: python3 -m ...)
#   3. Open http://127.0.0.1:8000/docs   (stop the server with Ctrl + C)

from fastapi import FastAPI

app = FastAPI()


# Postman: GET http://127.0.0.1:8000/greet/Asha
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}


# Postman: GET http://127.0.0.1:8000/ticket-price?age=20&student=true
@app.get("/ticket-price")
def ticket_price(age: int, student: bool = False):
    if age < 5:
        price = 0
    elif age <= 12 or age >= 65:
        price = 8
    elif student:
        price = 10
    else:
        price = 12
    return {"age": age, "student": student, "price": price}
