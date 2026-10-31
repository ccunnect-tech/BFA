# 2. Setup: install FastAPI

Python packages (like FastAPI) are installed with `pip`. We install FastAPI
**once, globally**, so it works from any folder. There is nothing to activate.

> The Python from Class 1 (python.org) allows this. You do **not** need a
> virtual environment for this course.

## Steps (in the VS Code terminal)

1. Install FastAPI. Keep the quotes:

   | Mac | Windows |
   |-----|---------|
   | `pip3 install "fastapi[standard]"` | `pip install "fastapi[standard]"` |

   Or install from the list file in the `class-4` folder (it contains the same line):

   | Mac | Windows |
   |-----|---------|
   | `pip3 install -r requirements.txt` | `pip install -r requirements.txt` |

2. Check it worked:

   ```
   fastapi --version
   ```

   You should see a FastAPI CLI version number.

## Running a server

Go to the folder that holds the file, then:

```
fastapi dev main.py
```

Open the address it prints, `http://127.0.0.1:8000`, and the docs at `/docs`. In
`dev` mode the server **restarts every time you save** the file. Stop it with
`Ctrl + C`.

## Common problems

| Problem | Fix |
|---------|-----|
| `fastapi: command not found` (or "not recognized") | Run it through Python instead: `python3 -m fastapi dev main.py` (Mac) or `python -m fastapi dev main.py` (Windows). Or close and reopen VS Code and try again. |
| `pip` not found | Mac: use `pip3`. Windows: use `python -m pip install "fastapi[standard]"`. |
| `externally-managed-environment` error | Your Python is not the python.org one. Install it from python.org (see Class 1), or ask for help. |
| `Address already in use` | An old server is still running. `Ctrl + C` it, or use `fastapi dev main.py --port 8001`. |
| `No such file` for `main.py` | You are in the wrong folder. `cd` into the folder that holds the file. |

## Later in the course (optional idea)

Professional projects often use a **virtual environment** (`python -m venv .venv`)
so each project has its own packages. We skip it here to keep things simple.
