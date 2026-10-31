# 1. The big picture: client, server and API

A full-stack app has three parts. We build them one by one in this course.

```
FRONTEND  (what the user sees: a web page, React)
   |   asks: "give me the tasks"
   v
BACKEND   (a server: our FastAPI program, Python)
   |   reads and saves
   v
DATABASE  (where data is kept: a JSON file today, a real database later)
```

- **Client / frontend**: the part that asks. A browser page, a phone app.
- **Server / backend**: the part that answers. It holds the data and the rules.
- **API**: the list of questions the server understands, for example
  "`GET /tasks` gives you all tasks".
- **JSON**: the text format they use to talk. It looks like a Python dictionary.

```json
{"id": 1, "title": "Buy milk", "done": false}
```

In Class 3 you saw this in the Network panel. Today we build the server side.

## The four things a client can ask

| Method | Meaning | Example |
|--------|---------|---------|
| `GET` | give me data | `GET /tasks` |
| `POST` | here is new data, save it | `POST /tasks` |
| `PUT` | change this | `PUT /tasks/3` |
| `DELETE` | remove this | `DELETE /tasks/3` |

Today we use `GET`, `POST` and `DELETE`.

## Status codes (you already know two)

| Code | Meaning |
|------|---------|
| **200** | OK |
| **404** | not found |

FastAPI sends the right code for you.

## Key points

- The page asks, the server answers.
- An API is a menu of requests.
- Data travels as JSON.
