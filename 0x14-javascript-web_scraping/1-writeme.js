#!/usr/bin/node

const { writeFile } = require('fs');
writeFile(process.argv[2], process.argv[3], error => {
  if (error) throw error;
});
