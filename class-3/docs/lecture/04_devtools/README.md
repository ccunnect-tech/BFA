# 4. Opening DevTools

DevTools is a toolbox built into your browser. It lets you look inside any web
page: its HTML, its CSS, its JavaScript, and every network request. Every web
developer uses it every day.

## How to open it

| | Shortcut |
|---|----------|
| Mac | `Cmd + Option + I` |
| Windows | `F12` or `Ctrl + Shift + I` |
| Any computer | right-click the page, then choose **Inspect** |

Works the same in Chrome, Edge and Firefox. You can dock it to the right, the
bottom, or pop it out into its own window (the three-dot menu in DevTools).

## The four panels we use

| Panel | What it shows | We use it to |
|-------|---------------|--------------|
| **Elements** | the page's HTML and CSS | look at the structure, edit text and styles live |
| **Console** | a place to run JavaScript | run code, read `console.log` output and errors |
| **Sources** | the page's files and a debugger | read the scripts the page loaded |
| **Network** | every request the page makes | see files and data the page downloads |

The Console is topic 5. The Network panel is topic 6.

## Open an HTML file in the browser from the terminal

| Mac | Windows |
|-----|---------|
| `open index.html` | `start index.html` |

Or just double-click the file in Finder / File Explorer.

## Try it

1. Open any website and open DevTools with the shortcut above.
2. Click through the four panels once.
3. In **Elements**, double-click some heading text on the page and type something else. The page changes.
4. Refresh the page. Your change is gone.

Why? DevTools changes **your copy** of the page, in your browser only. The
real page lives on a server. Refreshing downloads it again.

## Key points

- DevTools opens with `Cmd + Option + I` (Mac) or `F12` (Windows).
- Elements, Console, Sources and Network are the four panels to know.
- Changes you make in DevTools never change the real website.
