# Welcome to the Course

A hands-on, task-based course where you learn by doing. There are no slides. **This repository is your course material.**

---

## About this course

This course is built around practice, not theory. You will write code, build real things and get comfortable working with modern tools, including AI.

You do not need any prior programming experience. You only need curiosity and a willingness to make mistakes and fix them.

## How it works

- **Live classes.** You work alongside the instructor and complete tasks during the session.
- **After-class tasks.** You finish additional tasks on your own, then submit them.
- **One repository.** Everything you need lives here. Tasks and materials are added to this repository as the course goes on.

Every student is expected to complete the tasks. Doing the work is how you learn.

## Before you begin

Finish the setup for your computer **before the first live class**. It takes about 35 to 50 minutes.

| Your computer | Setup guide |
|---------------|-------------|
| 🍎 **Mac** | [macOS setup instructions](class-1/docs/class-1-setup-mac.md) |
| 🪟 **Windows** | [Windows setup instructions](class-1/docs/class-1-setup-windows.md) |

At the end of the guide you will run a small check to confirm everything works, and send a screenshot to the course group.

> Don't skip this. If setup isn't done, you will spend class time fixing your laptop instead of learning.

## Class 2: Python fundamentals

**What we cover:** Python version, the `.py` file, print and input, variables and types, conditionals, loops and functions.

No extra setup is needed. Your Class 1 setup is enough.

**What is in the `class-2` folder**

| Folder | What it is |
|--------|------------|
| [`docs/`](class-2/docs) | Class slides |
| [`live-practice/`](class-2/live-practice) | Practice questions we solve together in class. Each file has the problem and the expected output in comments. Write your code under the comment. |
| [`homework/`](class-2/homework) | Three tasks to finish after class. Push your work to your GitHub repo. |

## Class 3: JavaScript and the web platform

**What we cover:** where JavaScript runs (browser and Node.js), browser DevTools and the Console, JavaScript inside a web page, running files with Node.js, and npm packages.

We do not relearn loops and functions. You port what you learned in Python, then run it in the browser Console and in Node.

No extra setup is needed. Chrome (or Edge) and the Node.js from Class 1 are enough.

**What is in the `class-3` folder**

| Folder | What it is |
|--------|------------|
| [`docs/`](class-3/docs) | Class slides, and the [`lecture/`](class-3/docs/lecture) notes and code we show in class (start at its README) |
| [`live-practice/`](class-3/live-practice) | Practice tasks we do together in class. Each file has the problem and the expected output in comments. |
| [`homework/`](class-3/homework) | Four tasks to finish after class: the three Class 2 Python tasks again in JavaScript (run with `node`), and a small interactive website. Extra optional tasks are in `homework/optional`. Push your work to your GitHub repo. |

Run a JavaScript file with `node file.js`. For the Console tasks, paste your code into the Console tab in DevTools.

## Class 4: Backend with FastAPI

**What we cover:** the big picture (frontend, backend, API, JSON), installing FastAPI, building simple routes (values in the URL, `POST`, a to-do API with list, add and delete), the free `/docs` page, a web page that calls your API, and how we will use AI to build the app.

You need Python from Class 1. We install FastAPI in class (`pip install "fastapi[standard]"`).

**What is in the `class-4` folder**

| Folder | What it is |
|--------|------------|
| [`docs/`](class-4/docs) | Class slides, and the [`lecture/`](class-4/docs/lecture) notes and code we show in class (start at its README) |
| [`live-practice/`](class-4/live-practice) | Three API tasks we do together in class. Each file has the problem and the expected output in comments. |
| [`homework/`](class-4/homework) | Three tasks to finish after class: an even numbers API, a temperature API and a notes API. Push your work to your GitHub repo. |

Install FastAPI once with `pip install -r class-4/requirements.txt` (Mac: `pip3`). Run an API file with `fastapi dev file.py`, then test it at `http://127.0.0.1:8000/docs`.

---

## What you need

- A laptop (Mac or Windows) with internet access
- About 2 GB of free disk space
- A free GitHub account (the setup guide shows you how to create one)

## Getting help

1. Check the **Troubleshooting** section at the bottom of your setup guide first: [macOS](class-1/docs/class-1-setup-mac.md#troubleshooting) or [Windows](class-1/docs/class-1-setup-windows.md#troubleshooting).
2. Ask in the course group.
3. When you ask, include your operating system, what you did, and the **full** error message (copy-paste or screenshot).

---

Ready? Start with the setup guide for your computer: **[macOS](class-1/docs/class-1-setup-mac.md)** or **[Windows](class-1/docs/class-1-setup-windows.md)**.
