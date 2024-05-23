#!/usr/bin/node
// Computes the number of tasks completed by user id

const request = require('request');

request(process.argv[2], (err, response) => {
  if (!err) {
    const todoList = JSON.parse(response.body);
    const count = {};
    for (const item of todoList) {
      if (item.completed) {
        count[item.userId] = (count[item.userId] || 0) + 1;
      }
    }
    console.log(count);
  } else {
    console.log(err);
  }
});
