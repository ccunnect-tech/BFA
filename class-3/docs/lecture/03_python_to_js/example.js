// example.js - JavaScript. Run it:  node example.js   (Mac and Windows)
// Same program as example.py. Compare the two side by side.

// variables (const cannot change, let can)
const name = "Asha";
const age = 21;
const isStudent = true;          // true / false

// template string (backticks and ${ })
console.log(`${name} is ${age}`);

// if / else if / else, && || !
if (age >= 18 && isStudent) {
  console.log("Adult student");
} else if (age >= 18) {
  console.log("Adult");
} else {
  console.log("Minor");
}

// for loop
for (let i = 0; i < 3; i++) {
  console.log(i);
}

// function
function add(a, b) {
  return a + b;
}

console.log(add(3, 4));

// array and object
const fruits = ["apple", "mango"];
const person = { name: "Asha", city: "Toronto" };
console.log(fruits[0], person.city);

// === compares values (strict). Prefer it over ==
console.log(5 === 5);
