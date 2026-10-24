# 5. The Console

The Console is a place inside DevTools where you can **type JavaScript and run
it right away**. It also shows messages and errors from the page.

## Open it

1. Open any website, then open DevTools:
   - Mac: `Cmd + Option + I`
   - Windows: `F12` or `Ctrl + Shift + I`
2. Click the **Console** tab.
3. Click next to the `>` sign, type, and press **Enter**.

## What to type

The file [`console.js`](console.js) has every command below. Paste them one at
a time (or line by line) into the Console.

| Type this | What happens |
|-----------|--------------|
| `2 + 3` | the Console prints the result: `5` |
| `document.title` | prints the title of the page you are on |
| `console.log("hi")` | prints `hi` |
| `console.warn("careful")` | a yellow warning |
| `console.error("oops")` | a red error message |
| `console.table([{ a: 1 }, { a: 2 }])` | a small table |
| `nope` | `ReferenceError: nope is not defined` |

## Reading an error

A red error tells you three things: **what** went wrong
(`ReferenceError: nope is not defined`), **which file** and **which line**.
Click the file and line link on the right to jump to the code. Reading the
error message is the first step of fixing any bug.

## Handy habits

- **Up arrow** brings back the last command. Press it to repeat or fix one.
- `Ctrl + L` (Windows) / `Cmd + K` (Mac) clears the Console.
- Type `document.` and the Console suggests what comes next.
- Multi-line code: paste it in, or press `Shift + Enter` for a new line.

## Same thing in Node

`console.log` also works in Node, in your terminal. Only the browser has
`document`. See topics 2 and 9.

## Key points

- The Console runs JavaScript on the page you are looking at.
- `console.log`, `console.warn` and `console.error` print messages.
- Errors show the message, the file and the line number.
