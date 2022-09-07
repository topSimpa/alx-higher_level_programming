#!/usr/bin/node
const process = require('process');

let prod = 1;
function factorial (n) {
  if (n <= 1 || isNaN(n)) {
    return 1;
  } else {
    prod = prod * n;
    factorial(--n);
    return prod;
  }
}

console.log(factorial(parseInt(process.argv[2])));
