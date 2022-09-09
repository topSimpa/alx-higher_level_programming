#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let count = 0;
  while (list[i]) {
    if (list[i++] === searchElement) {
      count++;
    }
  }
  return count;
};
