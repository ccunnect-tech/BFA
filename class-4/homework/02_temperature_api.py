# HOW TO RUN
#   1. One time only, install FastAPI:  pip install "fastapi[standard]"
#      (Mac: pip3 install "fastapi[standard]")
#   2. Open the VS Code terminal in this file's folder and run:  fastapi dev 02_temperature_api.py
#      (if "fastapi" is not found:  python -m fastapi dev 02_temperature_api.py   Mac: python3 -m ...)
#   3. Open http://127.0.0.1:8000/docs   (stop the server with Ctrl + C)

# Homework 2: Temperature API
# ------------------------------------------------------------
# TOPICS: query parameters, float, functions, if / elif / else
# This is the temperature task from Class 2, now as an API.
#
# PROBLEM
# 1. Write a function c_to_f(celsius) that RETURNS celsius * 9 / 5 + 32.
# 2. Add the route  GET /temperature  with a float query parameter celsius.
# 3. Return a dict with celsius, fahrenheit and feeling. The feeling is "Hot"
#    if celsius is above 30, "Cold" if it is below 10, otherwise "Nice".
#
# RUN
#   fastapi dev 02_temperature_api.py
#
# EXPECTED OUTPUT
#   /temperature?celsius=35                  {"celsius":35.0,"fahrenheit":95.0,"feeling":"Hot"}
#   /temperature?celsius=20                  {"celsius":20.0,"fahrenheit":68.0,"feeling":"Nice"}
#   /temperature?celsius=0                   {"celsius":0.0,"fahrenheit":32.0,"feeling":"Cold"}
#   /temperature                             422 error (celsius is required)
# ------------------------------------------------------------
from fastapi import FastAPI

app = FastAPI()

# POSTMAN: once you write the routes, call them (fastapi dev <this file> must be running):
#   GET    http://127.0.0.1:8000/temperature?celsius=35
#   GET    http://127.0.0.1:8000/temperature?celsius=20
# Write your code below this line

