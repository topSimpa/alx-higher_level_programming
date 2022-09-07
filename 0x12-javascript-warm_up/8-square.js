#!/usr/bin/node
const process = require('process');
if (parseInt(process.argv[2])) {
  let x = parseInt(process.argv[2]);
  const y = x;
  while (x > 0) {
    console.log('X'.repeat(y));
    x--;
  }
} else {
  console.log('Missing size');
}
