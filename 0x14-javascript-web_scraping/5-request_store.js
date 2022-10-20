#!/usr/bin/node
// this script get the content of a webpage and then write to file

const { writeFile } = require('fs');
const request = require('request');

request(process.argv[2], function (err, resp, body) {
  if (err) {
    console.log(err);
  } else if (resp.statusCode === 200) {
    writeFile(process.argv[3], body, { encoding: 'utf8' }, err => {
      if (err) throw err;
    });
  }
});
