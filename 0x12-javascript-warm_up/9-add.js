#!/usr/bin/node

const { argv } = require('node:process');

const a = +argv[2];
const b = +argv[3];

function add (a, b) {
  const sum = a + b;
  return sum;
}
console.log(add(a, b));
