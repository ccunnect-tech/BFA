// hello.js - run it:  node hello.js
// Node runs JavaScript in the terminal, outside the browser.

console.log("Hello from Node");
console.log(2 + 3);

// Node has no page, so there is no document or window.
console.log(typeof document);   // undefined
console.log(typeof window);     // undefined

// Node has its own tools instead.
console.log(process.version);   // your Node version
console.log(process.platform);  // darwin, win32 or linux
console.log(process.cwd());     // the folder you ran it from
