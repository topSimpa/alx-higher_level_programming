#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  const nlist = [];
  while (len >= 0) {
    nlist.push(list[len--]);
  }
  return nlist;
};
