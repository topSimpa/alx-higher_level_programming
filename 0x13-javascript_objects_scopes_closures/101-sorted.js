#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = { };
for (const property in dict) {
  if (dict[property] in newDict) {
    newDict[dict[property]].push(property);
  } else {
    newDict[dict[property]] = [property];
  }
}

console.log(newDict);
