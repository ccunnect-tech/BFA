# 8. A web page that talks to your API

Files: [`main.py`](main.py), [`tasks.json`](tasks.json) and [`index.html`](index.html).
The tasks are saved in `tasks.json`, the same way as topic 6.

In Class 3 you made a page react to clicks. Now the page will **ask our server
for its data**. This is the full-stack idea: frontend + backend. In the later
classes we build the page with React and connect it the same way.

## Steps

1. Run the API: `fastapi dev main.py` (leave it running).
2. Open `index.html` in the browser (`open index.html` on Mac,
   `start index.html` on Windows, or double-click).
3. Click **Load tasks**. The list comes from your Python server.
4. Type a title and click **Add task**. Open `tasks.json` next to it: the new
   task is written into the file. Refresh the page and it is still there.
5. Open DevTools, Network tab, and click the buttons. You see the requests going
   to your own server.

## The key line

```js
const response = await fetch("http://127.0.0.1:8000/tasks");
const tasks = await response.json();
```

`fetch` sends the request. `.json()` turns the answer into a JavaScript array.
You do not need to memorise this. You will ask AI to write the fetch code and
you will recognise it.

## CORS: the block of extra lines in `main.py`

Browsers block a page from talking to a different server unless the server says
it is allowed. That is **CORS**. The block in `main.py` says "allowed". Copy it
into every API that a web page will call. If you forget, the Console shows a red
`CORS policy` error.

## Key points

- The page is the client, FastAPI is the server, JSON is what they say.
- Red CORS error in the Console means: add the CORS block to the server.
