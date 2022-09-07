#!/usr/bin/node
const process = require('process');

function secondSmallest (arr) {
  if (arr[0] && arr[1]) {
    arr = arr.sort(function (a, b) { return b - a; });
    return arr[1];
  } else {
    return (0);
  }
}

console.log(secondSmallest(process.argv.slice(2)));
