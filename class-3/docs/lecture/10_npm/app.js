// 10 - npm and packages
// Setup (once, in this folder):
//   npm init -y
//   npm install dayjs
// Then run:  node app.js
const dayjs = require("dayjs");

const today = dayjs();
console.log(today.format("MMM D"));
