#!/usr/bin/node
let call = 0;

exports.logMe = function (item) {
  console.log(call++, ':', item);
};
