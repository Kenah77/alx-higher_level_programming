#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const completed = {};

request(apiUrl, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  const tasks = JSON.parse(body);
  tasks.forEach((task) => {
    if (task.completed && completed[task.userId] === undefined) {
      completed[task.userId] = 1;
    } else if (task.completed) {
      completed[task.userId] += 1;
    }
  });
  console.log(completed);
});
