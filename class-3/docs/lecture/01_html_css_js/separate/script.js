// script.js - JavaScript: the behaviour (electricity and switches)
// It says WHAT HAPPENS when something occurs. Delete the script tag and the button does nothing.
const title = document.querySelector("#title");
const btn = document.querySelector("#btn");

btn.addEventListener("click", () => {
  title.textContent = "You clicked the button!";
  console.log("button clicked");
});
