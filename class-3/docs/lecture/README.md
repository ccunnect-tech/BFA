# Class 3 lecture notes: JavaScript and the web

Everything we show in class lives here, one numbered folder per topic. Each
folder has a `README.md` with the notes and the files we run. The numbers match
the headings on the slides (`docs/class-3-slides.pptx`).

> Class 2 taught the programming basics in Python (variables, conditions, loops,
> functions). This class does **not** teach them again in JavaScript. We look at
> the **platform**: where JavaScript runs, how to use the browser tools, and
> what Node.js and npm are.

## Topics

| # | Folder | What you learn |
|---|--------|----------------|
| 1 | [`01_html_css_js`](01_html_css_js) | What is on a web page: HTML, CSS and JavaScript, in one file or in separate files |
| 2 | [`02_browser_vs_node`](02_browser_vs_node) | One language, two places to run it |
| 3 | [`03_python_to_js`](03_python_to_js) | The same program in Python and JavaScript, side by side |
| 4 | [`04_devtools`](04_devtools) | Opening the browser DevTools and the four panels we use |
| 5 | [`05_console`](05_console) | The Console: run code, read logs and errors |
| 6 | [`06_network`](06_network) | The Network panel: every request a page makes |
| 7 | [`07_js_in_a_page`](07_js_in_a_page) | How JavaScript gets into a page (the script tag) |
| 8 | [`08_dom`](08_dom) | The DOM: find elements, change text, react to clicks |
| 9 | [`09_node`](09_node) | Node.js: run JavaScript in the terminal |
| 10 | [`10_npm`](10_npm) | npm: install packages other people wrote |

Study them in order. Topics 1 to 8 are in the browser, 9 and 10 are Node.js.

## Mac and Windows cheat sheet

| What | Mac | Windows |
|------|-----|---------|
| Open browser DevTools | `Cmd + Option + I` | `F12` or `Ctrl + Shift + I` |
| Open an HTML file from the terminal | `open index.html` | `start index.html` |
| Run a Python file | `python3 file.py` | `python file.py` |
| Run a JavaScript file | `node file.js` | `node file.js` |
| Check Node and npm | `node --version`, `npm --version` | `node --version`, `npm --version` |
| Stop a running program | `Ctrl + C` | `Ctrl + C` |

Run all terminal commands from the **VS Code terminal** (Terminal, New Terminal),
inside the folder that holds the file. Not sure where you are? Type `pwd` (Mac)
or `cd` (Windows) to see the current folder, and `cd folder-name` to go into one.
Or right-click a folder in VS Code and choose **Open in Integrated Terminal**.

## Before you start

- Chrome or Edge installed (Firefox also works).
- Node.js and npm installed in Class 1. Check with `node --version`.
- If a command is not found, see the Troubleshooting section of your Class 1
  setup guide, then restart VS Code.

## Practice

The practice tasks are in the folders next to this one:
[`../../live-practice`](../../live-practice) and [`../../homework`](../../homework).
