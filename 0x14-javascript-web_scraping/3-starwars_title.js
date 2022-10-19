#!/usr/bin/node
// send a request to star wars api

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const text = JSON.parse(body);
    console.log(text.title);
  }
});
