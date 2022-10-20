#!/usr/bin/node
// send a request to star wars api

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const todos = JSON.parse(body);

    let user;
    let task;
    const employeeTask = {};
    for (user = 0; (user + 1) * 20 <= 200; user++) {
      let sum = 0;
      for (task = 0; task < 20; task++) {
        if (todos[(user * 20) + task].completed === true) {
          sum++;
        }
      }
      if (sum > 0) {
        employeeTask[user + 1] = sum;
      }
    }
    console.log(employeeTask);
  }
});
