#!/usr/bin/node
const dict = require('./101-data.js').dict;

const newDict = {};

Object.entries(dict).forEach((entry) => {
  if (newDict[entry[1]] === undefined) {
    newDict[entry[1]] = [entry[0]];
  } else {
    newDict[entry[1]].push(entry[0]);
  }
});

console.log(newDict);
