#!/usr/bin/node
const process = require('process');
if (parseInt(process.argv[2])) {
  let x = parseInt(process.argv[2]);
  while (x > 0) {
    console.log('C is fun');
    x--;
  }
} else {
  console.log('Missing number of occurrences');
}
