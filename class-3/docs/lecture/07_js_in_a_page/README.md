# 7. JavaScript in a page

Topic 1 showed that JavaScript can sit inside a page or in its own file. This
topic looks at how a page **loads** a JavaScript file.

## The files

| File | What it does |
|------|--------------|
| [`index.html`](index.html) | a heading, a button, a paragraph, and one `<script>` tag |
| [`app.js`](app.js) | prints two lines to the Console |

The page links the script with:

```html
<script src="app.js"></script>
```

`src` is the path to the file. The browser downloads `app.js` (you can see it
as a row in the Network panel) and runs it.

## Where does the script tag go?

Put it **last in the `<body>`**, just before `</body>`.

The browser reads a page from top to bottom. If your script runs before the
`<h1>` or the button exists, it cannot find them. Placing the tag last means the
whole page is already there.

## Try it

1. Open the page:
   - Mac: `open index.html`
   - Windows: `start index.html`
2. Open DevTools and the Console. You should see:
   ```
   app.js loaded
   My page
   ```
3. Open the **Network** tab, refresh, and find the `app.js` row.
4. **Break it on purpose:** change `src="app.js"` to `src="app2.js"` and refresh.
   The Console shows a red `404` error: the browser could not find the file.
   Change it back.

## What the code means

```js
console.log("app.js loaded");     // prints a message to the Console
console.log(document.title);      // document is the whole page, .title is its title
```

`document` is the page as JavaScript sees it. Topic 8 shows how to use it.

## Key points

- A page loads JavaScript with `<script src="file.js"></script>`.
- Put the script tag last in the body so the page exists first.
- A wrong path gives a 404 in the Console and Network.
