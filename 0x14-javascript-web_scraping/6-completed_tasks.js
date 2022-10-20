#!/usr/bin/node
// send a request to star wars api

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const todos = JSON.parse(body);

    let task;
    let work;
    const employeeTask = {};
    for (task in todos) {
      work = todos[task];
      if (work.completed) {
        if (employeeTask[work.userId] === undefined) {
          employeeTask[work.userId] = 1;
        } else {
          employeeTask[work.userId]++;
        }
      }
    }
    console.log(employeeTask);
  }
});
