# 9. How we will build with AI

You do **not** need to know every line of code to build an app. You need to:

1. Know what each piece is for (you do, after today).
2. Ask AI for one small piece at a time.
3. Run it, test it, and read what it wrote.

## The loop

```
describe it  ->  AI writes it  ->  run it  ->  does it work?
     ^                                              |
     |------- paste the error or say what is wrong -|
```

## Writing a good request (a prompt)

Say **what** you want, **where** (which file), and **how it should look**.

Weak: `make my api better`

Better:

```
I have a FastAPI file main.py with a list called notes. Add a route
GET /notes/count that returns how many notes there are, as JSON like
{"count": 2}. Keep the code simple and add a short comment.
```

## Habits that work

| Do | Why |
|----|-----|
| Ask for **one small change** at a time | Easy to test, easy to undo |
| **Run it** after every change | You find the problem right away |
| Test in **/docs** | You see the real answer and status code |
| **Paste the full error** back to the AI | The error tells it what is wrong |
| Ask "explain this line in simple words" | You learn and stay in control |
| Save your work with **git** before big changes | You can go back |

## Never

- Paste secrets (passwords, API keys) into a prompt.
- Run code you did not read at all.

## Try it

Use any AI assistant:

1. Give it the `06_todo_crud/main.py` code and ask it to add `GET /tasks/count`.
2. Paste its answer into your file, run the server, and test it in `/docs`.
3. Ask it: "explain each line you added in simple words".
