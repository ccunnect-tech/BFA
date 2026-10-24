# Live practice 1: Console explorer

**Topics:** DevTools, the Console, `document`

## Problem

1. Open any website (Wikipedia is a good one) and open DevTools:
   - Mac: `Cmd + Option + I`
   - Windows: `F12` or `Ctrl + Shift + I`
   - Any computer: right-click the page, then **Inspect**.
2. Go to the **Console** tab. Run `document.title` and read the answer.
3. Store the main heading in a variable: `h = document.querySelector("h1")`
4. Change its text: `h.textContent = "Hello BFA"`. Look at the page.
5. Refresh the page. What happened to your change? Write the answer below.

## Expected output (your Console should look like this)

```
> document.title
'Wikipedia, the free encyclopedia'
> h = document.querySelector("h1")
> h.textContent = "Hello BFA"
'Hello BFA'
```

## Your answer: what happened after the refresh, and why?

(write here)
