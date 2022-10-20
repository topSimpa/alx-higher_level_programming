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
    let sum = 0;
    let userId = todos[0].userId;
    const employeeTask = {};
    for (user in todos) {
      if (user === todos.length - 1) {
        if (todos[user].completed) {
          sum++;
        }
        if (sum > 0) {
          employeeTask[userId] = sum;
        }
        console.log(employeeTask);
        break;
      }
      if (todos[user].userId !== userId) {
        if (sum > 0) {
          employeeTask[userId] = sum;
        }
        userId = todos[user].userId;
        sum = 0;
      }
      if (todos[user].completed) {
        sum++;
      }
    }
  }
});
