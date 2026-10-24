// Homework 3: Guess the number
// ------------------------------------------------------------
// TOPICS: variables, while loop, break, if / else if / else, template strings
// This is Homework 3 from Class 2. Do it again in JavaScript, and run it
// with Node:  node 03_guess_the_number.js
//
// PROBLEM
// Node has no input() like Python, so the guesses are in a list (array).
// Use a while loop to go through the guesses one by one. Count the tries in a
// variable. For each wrong guess print Too low or Too high. When a guess is
// right, print how many tries it took and break out of the loop.
//
// HINT: guesses[index] is the current guess. Add 1 to index every round.
//
// EXPECTED OUTPUT (with the guesses below)
//   Guess: 3
//   Too low
//   Guess: 9
//   Too high
//   Guess: 7
//   Correct! You took 3 tries.
// ------------------------------------------------------------
const secret = 7;
const guesses = [3, 9, 7];

// Write your code below this line

