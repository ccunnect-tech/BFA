# 3. Python to JavaScript

You already know how to program from Class 2. JavaScript has the same ideas
with a different spelling. This page is a **translation table**, not a new
lesson in programming.

## Run both files

[`example.py`](example.py) and [`example.js`](example.js) are the same program.
Run them from this folder in the VS Code terminal:

| | Mac | Windows |
|---|-----|---------|
| Python | `python3 example.py` | `python example.py` |
| JavaScript | `node example.js` | `node example.js` |

Both print the same lines (Python prints `True`, JavaScript prints `true`):

```
Asha is 21
Adult student
0
1
2
7
apple Toronto
True        (true in JavaScript)
```

## Side by side

| Idea | Python | JavaScript |
|------|--------|------------|
| Variable | `name = "Asha"` | `const name = "Asha";` or `let name = "Asha";` |
| Print | `print(x)` | `console.log(x)` |
| Text with values | `f"{name} is {age}"` | `` `${name} is ${age}` `` (backticks) |
| Booleans | `True`, `False` | `true`, `false` |
| Nothing | `None` | `null` (and `undefined` for "no value yet") |
| If | `if age >= 18:` | `if (age >= 18) {` |
| Else if | `elif` | `else if` |
| And, or, not | `and`, `or`, `not` | `&&`, `\|\|`, `!` |
| Equal | `==` | `===` (strict: also compares the type) |
| For loop | `for i in range(3):` | `for (let i = 0; i < 3; i++) {` |
| Function | `def add(a, b):` | `function add(a, b) {` |
| List | `[1, 2, 3]` | `[1, 2, 3]` (called an array) |
| Dictionary | `{"name": "Asha"}` | `{ name: "Asha" }` (called an object) |
| Item of a list | `fruits[0]` | `fruits[0]` |
| Item of a dict | `person["city"]` | `person.city` |
| Blocks | indentation | braces `{ }` |
| Line end | nothing | semicolon `;` (optional, we use it) |
| Comment | `# text` | `// text` |

## The three changes that trip people up

1. **Braces and parentheses.** Python uses a colon and indentation. JavaScript
   uses `( )` around the condition and `{ }` around the block. Indenting is
   still good style, but JavaScript does not need it.
2. **`const` and `let`.** `const` cannot be reassigned, `let` can. Use `const`
   by default. (You may see `var` in old code. Avoid it.)
3. **`===` instead of `==`.** `5 == "5"` is `true` in JavaScript (surprise!)
   because `==` converts types. `5 === "5"` is `false`. Always use `===`.

## Key points

- Same ideas, new spelling. Do not memorise the table, use it when you port code.
- `print` becomes `console.log`, `and` becomes `&&`, `elif` becomes `else if`.
- The practice tasks in class are Python programs you ported to JavaScript.
