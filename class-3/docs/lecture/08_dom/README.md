# 8. The DOM: the page as objects

When the browser loads HTML, it turns every tag into a JavaScript **object**.
That tree of objects is the **DOM** (Document Object Model). JavaScript can
find any object in it and change it. This is how pages become interactive.

`document` is the top of the tree.

## The files

| File | What it does |
|------|--------------|
| [`index.html`](index.html) | a heading, a paragraph, a list of three items (class `item`), two buttons |
| [`app.js`](app.js) | the six steps below, each printing to the Console |

## The six steps (in `app.js`)

### 1. `document` is the page

```js
console.log(document);
console.log(document.title);
```

### 2. Find one element by its id

```js
const title = document.getElementById("title");
```

### 3. Find one element with `querySelector`

`querySelector` takes any CSS selector: `#id` for an id, `.name` for a class, or a tag name.

```js
const info = document.querySelector("#info");        // by id
const firstItem = document.querySelector(".item");   // first one with that class
```

### 4. Find many elements

```js
const items = document.querySelectorAll(".item");    // every element with the class
const same = document.getElementsByClassName("item");
for (const item of items) {
  console.log(item.textContent);
}
```

| Method | Returns |
|--------|---------|
| `getElementById("x")` | one element |
| `querySelector("#x")` or `(".x")` | the first matching element |
| `querySelectorAll(".x")` | all matching elements |
| `getElementsByClassName("x")` | all elements with the class |

### 5. Change text with `textContent`

```js
console.log(info.textContent);                       // read it
info.textContent = "app.js changed this text.";      // set it
```

### 6. React to clicks with `addEventListener`

```js
changeBtn.addEventListener("click", () => {
  title.textContent = "You clicked the button!";
});
```

`addEventListener("click", function)` says: **when this thing is clicked, run
this function**. You give it the event name and the function. The function runs
every time the event happens, not just once.

The second button uses `classList.toggle("highlight")` to switch a CSS class on
and off, which turns the list items yellow.

## Try it

1. Open the page (`open index.html` on Mac, `start index.html` on Windows).
2. Open DevTools, Console. Read what `app.js` printed.
3. Click both buttons.
4. **Experiment** in the Console on the same page:
   ```js
   title.textContent = "Hello BFA"
   document.body.style.background = "lightyellow"
   document.querySelectorAll(".item").length
   ```
5. Refresh. Everything is back: you only changed your copy of the page.

## Key points

- The DOM is the page as JavaScript objects. `document` is the top.
- Find elements with `getElementById`, `querySelector`, `querySelectorAll`.
- `textContent` reads and changes the text of an element.
- `addEventListener` runs a function when an event (like a click) happens.
- This is a small taste. Class 5 builds real pages with HTML, CSS and JavaScript.
