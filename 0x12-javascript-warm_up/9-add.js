#!/usr/bin/node

const { argv } = require('node:process');

let a = +argv[2];
let b = +argv[3];

function add(a,b) {
  sum = a + b;
  return sum;
}
console.log(add(a, b));
