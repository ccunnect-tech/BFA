# 10. npm and packages

**npm** (Node Package Manager) is installed together with Node.js. It downloads
**packages**: code that other developers wrote and shared, so you do not have
to write everything yourself. React, the tool we use in Class 6, is one.

## Check it

```
npm --version
```

Same command on Mac and Windows.

## The three things npm creates

| Name | What it is |
|------|------------|
| `package.json` | a list of what your project uses (name, version, dependencies) |
| `node_modules/` | the folder where the downloaded packages live (can be huge) |
| `package-lock.json` | the exact versions installed, so everyone gets the same ones |

**Never push `node_modules` to GitHub.** It is big and anyone can recreate it
with `npm install`. Our `.gitignore` already skips it.

## Make a project

In an empty folder:

```
npm init -y
```

This creates `package.json`. Open it and read it.

## Install a package

```
npm install dayjs
```

`dayjs` is a small package for working with dates. After the command,
`package.json` lists it under `dependencies` and a `node_modules` folder appears.

## Use it

[`app.js`](app.js):

```js
const dayjs = require("dayjs");

const today = dayjs();
console.log(today.format("MMM D"));
```

Run it:

```
node app.js
```

Output, for example: `Oct 24`.

## Download this folder's packages

This folder has a `package.json` that already lists `dayjs`, but not the
`node_modules` folder. To get the packages, run this in the folder:

```
npm install
```

That reads `package.json` and downloads everything it lists. This is what you
do whenever you clone a project from GitHub.

## Scripts

`npm run <name>` runs a command listed in the `scripts` part of `package.json`.
Vite, the React setup tool, uses `npm run dev` to start the app (you do this in
live practice 3).

## Commands, Mac and Windows

All identical:

| Task | Command |
|------|---------|
| Check npm | `npm --version` |
| Start a project | `npm init -y` |
| Install a package | `npm install <name>` |
| Install everything in package.json | `npm install` |
| Run a script | `npm run <name>` |

## Key points

- npm downloads packages other people wrote.
- `package.json` is the list, `node_modules` is the download folder.
- Never push `node_modules`. Run `npm install` to rebuild it.
