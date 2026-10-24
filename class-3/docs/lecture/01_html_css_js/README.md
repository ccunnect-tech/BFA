# 1. What is on a web page

Every website you have ever used is built from three languages. Think of
building a house:

| Language | Job | The house |
|----------|-----|-----------|
| **HTML** | structure: what is on the page | pillars, bricks and walls |
| **CSS** | looks: colours, fonts, spacing | paint and interior |
| **JavaScript** | behaviour: what happens when you click | electricity and switches |

Take one away and the page still loads, but something is missing:
no CSS means a plain white page, no JavaScript means buttons do nothing.

## The same page, two ways

Both versions look and behave **exactly the same**. Only the file layout differs.

### `separate/` : three files (how real projects do it)

| File | Language | What is inside |
|------|----------|----------------|
| [`index.html`](separate/index.html) | HTML | a heading, a paragraph, a button. It links the other two files. |
| [`style.css`](separate/style.css) | CSS | yellow background, red heading, bigger button |
| [`script.js`](separate/script.js) | JavaScript | when the button is clicked, change the heading text |

`index.html` brings the others in with two lines:

```html
<link rel="stylesheet" href="style.css" />   <!-- the look -->
<script src="script.js"></script>            <!-- the behaviour -->
```

### [`combined.html`](combined.html) : everything in one file

HTML sits in the `<body>`, CSS inside a `<style>` tag, JavaScript inside a
`<script>` tag. Fine for a quick demo. For real projects, separate files are
easier to read, reuse and share.

## Try it

1. Open the page in your browser:
   - Mac: `open separate/index.html`
   - Windows: `start separate/index.html`
   - Or double-click the file in your file explorer.
2. Click the button. The heading changes.
3. Open DevTools (`Cmd + Option + I` / `F12`) and look at the Console: you will see `button clicked`.
4. **Experiment**
   - In `index.html`, delete the `<link ... style.css>` line and refresh: the page loses its look.
   - Delete the `<script src="script.js">` line and refresh: the button does nothing.
   - Open `combined.html` and compare.

## Key points

- HTML = structure, CSS = looks, JavaScript = behaviour.
- A page can keep all three in one file or in separate files.
- The browser reads the HTML first, then loads the CSS and JavaScript it points to.
- Put the `<script>` tag **last** in the body, so the page exists before the code runs (see topic 7).
