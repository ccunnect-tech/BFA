# Class 4 lecture notes: Backend with FastAPI

Everything we show in class lives here, one numbered folder per topic. Each
folder has a `README.md` with the notes and the files we run. The numbers match
the headings on the slides (`docs/class-4-slides.pptx`).

> The goal of this course is to **build a full-stack app with the help of AI**.
> Today we get the big picture, then build the **backend**: a small program
> that answers requests. We keep it simple. You do not need to memorise
> anything. You need to know what each piece is for, so you can ask AI for
> the right thing and understand what it gives you back.

## Topics

| # | Folder | What you learn |
|---|--------|----------------|
| 1 | [`01_client_server_api`](01_client_server_api) | The big picture: frontend, backend, API, JSON |
| 1b | [`01b_what_is_an_api`](01b_what_is_an_api) | What an API is, why we use one, and trying real APIs in Postman |
| 2 | [`02_setup`](02_setup) | Install FastAPI (globally, once) and run a server |
| 3 | [`03_hello_api`](03_hello_api) | Your first API: a route that returns JSON |
| 4 | [`04_path_and_query`](04_path_and_query) | Sending a value in the URL |
| 5 | [`05_post_and_models`](05_post_and_models) | Sending data to the server with `POST` |
| 6 | [`06_todo_crud`](06_todo_crud) | A to-do API that saves its data in a JSON file |
| 7 | [`07_swagger_docs`](07_swagger_docs) | The free `/docs` page to test your API |
| 8 | [`08_fetch_from_a_page`](08_fetch_from_a_page) | A web page that talks to your API |
| 9 | [`09_build_with_ai`](09_build_with_ai) | How we will use AI to build the app |

Study them in order. Every code folder (3 to 6 and 8) has a `main.py`. Run one
at a time, from inside its own folder.

## Mac and Windows cheat sheet

| What | Mac | Windows |
|------|-----|---------|
| Install FastAPI (once) | `pip3 install "fastapi[standard]"` | `pip install "fastapi[standard]"` |
| Or install from the list | `pip3 install -r ../../requirements.txt` | `pip install -r ..\..\requirements.txt` |
| Run the server | `fastapi dev main.py` | `fastapi dev main.py` |
| If `fastapi` is not found | `python3 -m fastapi dev main.py` | `python -m fastapi dev main.py` |
| Stop the server | `Ctrl + C` | `Ctrl + C` |
| Open the API docs | `http://127.0.0.1:8000/docs` | `http://127.0.0.1:8000/docs` |

Run all terminal commands from the **VS Code terminal** (Terminal, New Terminal),
inside the folder that holds `main.py`. FastAPI is installed once and works from
any folder. No virtual environment is needed.

## Before you start

- Python installed in Class 1. Check with `python3 --version` (Mac) or
  `python --version` (Windows).
- Chrome or Edge.
- No other setup. Topic 2 shows how to install FastAPI.

## Practice

The practice tasks are in the folders next to this one:
[`../../live-practice`](../../live-practice) and [`../../homework`](../../homework).
