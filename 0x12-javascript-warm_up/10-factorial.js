#!/usr/bin/node

const { argv } = require('node:process');

if (!argv[2] || isNaN(parseFloat(argv[2]))) {
  console.log(1);
} else {
  console.log(fact(Math.floor(parseFloat(argv[2]))));
}

function fact (a) {
  if (a === 1 || a === 0) {
    return 1;
  } else {
    return (a * fact(a - 1));
  }
}
