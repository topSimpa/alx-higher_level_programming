#!/usr/bin/node
// send request to a url

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
