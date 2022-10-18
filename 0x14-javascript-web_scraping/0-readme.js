#!/usr/bin/node
// prints out content of a file passed as parameter

const { readFile } = require('fs');
readFile(process.argv[2], 'utf8', (error, text) => {
  if (error) throw error;
  console.log(text);
});
