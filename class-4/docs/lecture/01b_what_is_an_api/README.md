# 1b. What is an API, and why do we use one?

## The idea

An **API** (Application Programming Interface) is a way for **one system to talk
to another** system. One side sends a **request**, the other sends back a
**response**, usually as JSON.

```
Your app / page  ----- request  GET /posts/1 ----->  Another system
                 <---- response  JSON -------------   (a server somewhere)
```

You already built one side of this: your FastAPI server answers requests, and
your web page asked it for tasks.

## Why APIs matter

- **Reuse instead of rebuild.** You do not build a map, a payment system or a
  news feed. You call someone's API that already does it.
- **Different systems can work together.** A React page, a phone app and a
  Python script can all use the same API, because they all speak HTTP and JSON.
- **The data stays in one place.** The server owns the data and the rules. Every
  client asks for what it needs.
- **Real apps are built from APIs.** Login, payments, weather, AI models: each is
  an API call.

## An API tester: Postman or Talend API Tester

A browser address bar can only do `GET`. An **API tester** lets you send any
request, with any method, headers and body, and see the full response.

| Tool | Where |
|------|-------|
| **Postman** | Desktop app (free account) or the web version |
| **Talend API Tester** | Chrome extension (also works in Edge) |

How to use either one:

1. Choose the method (`GET`, `POST`...).
2. Paste the URL.
3. Click **Send**.
4. Read the **status code** and the **body** (the JSON). For a `POST`, open
   **Body**, choose **raw** and **JSON**, and paste the JSON first.

You can call your own API (`http://127.0.0.1:8000/tasks`, with the server
running) in exactly the same way. Once we build our own API (topic 3 onwards),
every route in this lecture has a `# Postman:` comment with its URL.

## Two free sample APIs to try

### 1. JSONPlaceholder (fake posts, no key needed)

```
GET https://jsonplaceholder.typicode.com/posts/1
```

The response (JSON):

```json
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
```

Try also `/posts` (all posts, a list), `/posts/2`, and `/posts/9999` (what status
code do you get?).

### 2. NewsData.io (real news headlines, needs a free key)

```
GET https://newsdata.io/api/1/latest?apikey=YOUR_API_KEY
```

- `https://newsdata.io/api/1/latest` is the **path**.
- `apikey=...` is a **query parameter** (topic 4!). The key tells the service who
  you are.
- Use the key your instructor shares in class, or create your own free key at
  `newsdata.io`.
- The response has `status`, `totalResults`, a `results` list of articles (each
  with a `title`, `link`, `description`...) and `nextPage`.

### Real-world example: how a news website uses this

Open any news website. The page you see is built from data like the NewsData
response. The **frontend app** (React, in later classes) asks the API for the
latest articles, gets a **list of JSON objects**, and draws one card for each:

```
API response (JSON)                     What the frontend shows
-------------------                     -----------------------
results[0].image_url   ------------->   [ picture ]
results[0].title       ------------->   headline  (<h2>)
results[0].description ------------->   summary   (<p>)
results[0].link        ------------->   "Read more" link (<a href=...>)
results[1] ...         ------------->   the next card
```

The frontend does not store any news. It asks, receives the JSON, loops over
`results`, and shows each article. When the news changes, the next request
returns new JSON and the page updates, with no change to the frontend code.

This is the same thing our `fetch` page did in topic 8: ask the API, receive
JSON, show it. We will build this kind of page with React.

> **An API key is a password.** Never paste a real key into a file you push to
> GitHub or into a prompt for AI. That is why `YOUR_API_KEY` is written here
> instead of the real one.

## Try it

1. Send the JSONPlaceholder request. Find the `title` in the response.
2. Send the NewsData request with your key. How many `results` came back?
3. Look at one article in `results`. Which field would you use for a headline? For
   a picture? For a "Read more" link?
4. Remove the key from the URL and send again. What status code and message do
   you get?
5. Later, after topic 6: start `06_todo_crud/main.py` and call
   `GET http://127.0.0.1:8000/tasks` from the API tester.

## Key points

- An API is how systems talk to each other: request out, JSON back.
- An API tester sends any request and shows the full response.
- Most useful apps are built by calling other people's APIs.
