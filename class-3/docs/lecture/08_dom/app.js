// app.js - the DOM: the page as objects JavaScript can find and change.
// Open index.html in the browser, open DevTools, and read the Console.

// 1. The DOM is the whole page as objects. "document" is the top of it.
console.log(document);
console.log(document.title);                       // DOM demo

// 2. FIND one element by its id
const title = document.getElementById("title");
console.log(title);                                // <h1 id="title">...</h1>

// 3. FIND with querySelector: any CSS selector (#id, .class, tag)
const info = document.querySelector("#info");      // by id
const firstItem = document.querySelector(".item"); // first element with class "item"
console.log(info.textContent, "|", firstItem.textContent);

// 4. FIND many: querySelectorAll or getElementsByClassName
const items = document.querySelectorAll(".item");
console.log(items.length);                         // 3
for (const item of items) {
  console.log(item.textContent);                   // Apple, Banana, Mango
}
const sameItems = document.getElementsByClassName("item");
console.log(sameItems.length);                     // 3

// 5. CHANGE text with textContent (read it, or set it)
info.textContent = "app.js changed this text.";

// 6. EVENTS: addEventListener runs a function every time something happens
const changeBtn = document.querySelector("#changeBtn");
changeBtn.addEventListener("click", () => {
  title.textContent = "You clicked the button!";
  console.log("changeBtn clicked");
});

const highlightBtn = document.getElementById("highlightBtn");
highlightBtn.addEventListener("click", () => {
  for (const item of items) {
    item.classList.toggle("highlight");            // add or remove a CSS class
  }
});

// Refresh the page and everything is back: you only changed your copy.
