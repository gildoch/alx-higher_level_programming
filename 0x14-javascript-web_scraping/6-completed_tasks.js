#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, (error, _response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  body = JSON.parse(body);

  const userTaskCount = {};
  body.forEach(task => {
    if (task.completed) {
      if (userTaskCount[task.userId]) {
        userTaskCount[task.userId]++;
      } else {
        userTaskCount[task.userId] = 1;
      }
    }
  });

  console.log(userTaskCount);
});
