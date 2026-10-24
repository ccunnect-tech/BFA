# Live practice 3: npm and React setup

**Topics:** npm, `npm init`, creating a React app with Vite

## Problem

Do these in the terminal (VS Code: Terminal, New Terminal). The commands are
the same on Mac and Windows. Stop a running command with `Ctrl + C` on both.

1. Check that npm exists:

   ```
   npm --version
   ```

2. Make a folder for today and set it up as an npm project:

   ```
   mkdir class-3-npm
   cd class-3-npm
   npm init -y
   ```

   Open the new `package.json` file and read it.

3. Create a React app (if it asks questions, press Enter to take the
   default, and answer **No** to "install and start now"):

   ```
   npm create vite@latest my-react-app -- --template react
   ```

4. Go into the app, install its packages, and start it:

   ```
   cd my-react-app
   npm install
   npm run dev
   ```

5. Open the address it prints (Local: ...) in your browser.
   Stop the server with `Ctrl + C`.

## Expected output

```
$ npm --version
10.x.x

$ npm run dev
  VITE v8.x.x  ready in 475 ms
  Local:   http://localhost:5173/
```

The browser shows the Vite + React starter page.

## Notes

- `package.json` lists what a project uses. `npm install` fills a
  `node_modules` folder. Never push `node_modules` (our `.gitignore` already skips it).
- We build real React apps in Class 6.
