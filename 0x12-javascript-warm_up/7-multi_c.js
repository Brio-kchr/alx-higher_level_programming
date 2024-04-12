#!/usr/bin/node

const { argv } = require('node:process');

if (argv[2] && !isNaN(parseFloat(argv[2]))) {
  for (let a = 0; a < Math.floor(parseFloat(argv[2])); a++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
