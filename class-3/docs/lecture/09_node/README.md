# 9. Node.js runs JavaScript on your laptop

Node.js lets you run JavaScript **outside the browser**, in your terminal. It
uses the same engine as Chrome (V8). You installed it in Class 1.

## Check it

```
node --version
```

You should see a version like `v22.x.x`. Same command on Mac and Windows.

## Run a file

[`hello.js`](hello.js) is a short program. In the VS Code terminal, inside this
folder:

```
node hello.js
```

Expected output (the last three lines show your own computer):

```
Hello from Node
5
undefined
undefined
v22.12.0
darwin
/path/to/your/folder
```

| Line | What it shows |
|------|---------------|
| `undefined` (twice) | there is no `window` and no `document` in Node, because there is no web page |
| `process.version` | your Node version |
| `process.platform` | `darwin` on Mac, `win32` on Windows, `linux` on Linux |
| `process.cwd()` | the folder you ran the program from |

## Type JavaScript live (the REPL)

Run `node` on its own, with no file name:

```
node
> 2 + 3
5
> "hello".toUpperCase()
'HELLO'
> .exit
```

This is the terminal version of the browser Console. Type `.exit` (or press
`Ctrl + C` twice) to leave.

## Browser vs Node (recap of topic 2)

| Browser | Node.js |
|---------|---------|
| has `document`, `window` | has `process`, `require`, `fs` |
| runs in a web page | runs in the terminal |
| open an `.html` file | `node file.js` |

## Commands, Mac and Windows

These are identical on both:

| Task | Command |
|------|---------|
| Node version | `node --version` |
| Run a file | `node hello.js` |
| Open the REPL | `node` |
| Leave the REPL | `.exit` |
| Stop a running program | `Ctrl + C` |

`node: command not found`? See the Troubleshooting section of your Class 1
setup guide, and restart VS Code.

## Why we need Node in this course

We do not use Node as a server here. In this course Node is the **tool that
runs our tools**: `npm` and the React build tools all run on Node (topic 10).

## Key points

- Node runs JavaScript in the terminal: `node file.js`.
- There is no `document` or `window` in Node.
- `node` alone gives you a live prompt to try code.
