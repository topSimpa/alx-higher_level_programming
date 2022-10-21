#!/usr/bin/node
// send a request to star wars api

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const film = JSON.parse(body);

    let actors;
    let char;
    for (char in film.characters) {
      actors = film.characters;
      request(actors[char], function (err, resp, bdy) {
        if (err) {
          console.log(err);
        } else if (resp.statusCode === 200) {
          const actor = JSON.parse(bdy);

          console.log(actor.name);
        }
      });
    }
  }
});
