#!/usr/bin/node
const list = require('./100-data.js').list;

const newList = list.map((val, ind) => {
  return (val * ind);
});

console.log(list);
console.log(newList);
