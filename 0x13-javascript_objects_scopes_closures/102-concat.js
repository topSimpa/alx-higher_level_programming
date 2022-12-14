#!/usr/bin/node
const fs = require('fs');
const buffer1 = (fs.readFileSync(process.argv[2])).toString();
const buffer2 = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], buffer1 + buffer2);
