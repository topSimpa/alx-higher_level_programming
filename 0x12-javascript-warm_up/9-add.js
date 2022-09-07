#!/usr/bin/node
const process = require('process');

function add (a, b) {
  return (a * b);
}

console.log(add(process.argv[2], process.argv[3]));
