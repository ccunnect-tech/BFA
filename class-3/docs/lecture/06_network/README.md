# 6. The Network panel

When you open a web page, your browser does not get it in one piece. It makes
a lot of small **requests**, and a server answers each one.

```
browser  ---- "give me /index.html" ---->  server
browser  <--- here is the HTML (200) ----  server
browser  ---- "give me /style.css"  ---->  server
browser  ---- "give me /app.js"     ---->  server
browser  ---- "give me /api/user"   ---->  server   <--- 404: not found
```

The Network panel shows every one of those requests, live.

## How to use it

1. Open any website and open DevTools (`Cmd + Option + I` on Mac, `F12` on Windows).
2. Go to the **Network** tab.
3. **Refresh the page.** Rows appear, one per request.

Example of what you will see:

| Method | URL | Status |
|--------|-----|--------|
| GET | /index.html | 200 |
| GET | /style.css | 200 |
| GET | /app.js | 200 |
| GET | /api/user | 404 |

## Reading a row

| Column | Meaning |
|--------|---------|
| **Name** | which file or URL was requested |
| **Method** | `GET` asks for something. `POST` sends something. |
| **Status** | the server's answer code (see below) |
| **Type** | document (HTML), stylesheet (CSS), script (JS), image, fetch... |
| **Size** | how big the download was |
| **Time** | how long it took |

Click a row to see its **Headers**, **Preview** and **Response**.

## Status codes to know

| Code | Meaning |
|------|---------|
| **200** | OK, here it is |
| **404** | not found (wrong URL, or the file does not exist) |
| **500** | the server broke |

## Try it

1. On a news or shopping site, refresh with the Network tab open. Read the
   count of requests at the bottom of the panel. One page can make 50 to 200.
2. Click the **Size** column to sort. Which file is the biggest?
3. Type `.js` in the filter box. Which scripts did the page load?
4. Click an image row and open **Preview**.

## Why this matters

- The first request returns only the HTML. The browser reads it and then asks
  for every CSS file, script, image and font it mentions.
- In **Class 4** we build the server side of this conversation with FastAPI.
- In **Class 7** your React page will request data from that server.

## Key points

- A page is many requests, not one.
- The browser asks, a server answers, and Network shows both.
- 200 is good, 404 is missing, 500 is a server error.
