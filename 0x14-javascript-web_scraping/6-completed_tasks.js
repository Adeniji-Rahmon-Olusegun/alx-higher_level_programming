#!/usr/bin/node

const req = require('request');

const apiEndpoint = process.argv[2];

req(apiEndpoint, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const tasks = JSON.parse(body);
    const finishedTasks = {};

    tasks.forEach(todo => {
      if (todo.completed) {
        if (!finishedTasks[todo.userId]) {
          finishedTasks[todo.userId] = 1;
        } else {
          finishedTasks[todo.userId]++;
        }
      }
    });

    console.log(finishedTasks);
  }
});
