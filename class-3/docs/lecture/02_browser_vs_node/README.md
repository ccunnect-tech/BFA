# 2. One language, two places

JavaScript is one language that runs in two places:

- **The browser** (Chrome, Edge, Firefox): makes web pages interactive.
- **Node.js**: runs JavaScript in your terminal, outside any browser.

Both use the same engine (Google's **V8**) and the same language rules. What
differs is the **built-in tools** each place gives you.

| | Browser | Node.js |
|---|---------|---------|
| Runs inside | a web page | your terminal |
| Special objects | `document`, `window` | `process`, `require`, `fs` |
| Can change the page | yes | no page at all |
| Can read your files | no (security) | yes |
| Main use | websites | servers, tools, scripts, build tools |
| How to run | open an `.html` file | `node file.js` |

Why the browser cannot read your files: any website could otherwise read your
documents. The browser keeps every page in a safe box.

## Try it: where am I?

[`where_am_i.js`](where_am_i.js) asks the question "which of these exist here?"
and prints the answer. Run the **same code in both places**:

**In Node** (terminal, in this folder):

```
node where_am_i.js
```

Expected output:

```
window:   undefined
document: undefined
process:  object
```

**In the browser** (open any website, press `Cmd + Option + I` / `F12`,
go to the Console, paste the file's three `console.log` lines, press Enter):

```
window:   object
document: object
process:  undefined
```

The answers are mirror images. That is the whole story of this topic.

## Key points

- Same language, different built-in tools.
- `document` and `window` exist only in the browser. `process` and `require` exist only in Node.
- In this course the browser is for what users see (Classes 5 to 7), and Node is
  the tool that runs our build commands (npm, React tooling).
