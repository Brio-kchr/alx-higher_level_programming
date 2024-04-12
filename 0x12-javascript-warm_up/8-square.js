#!/usr/bin/node

const { argv } = require('node:process');

if (argv[2] && !isNaN(parseFloat(argv[2]))) {
  for (let a = 0; a < Math.floor(parseFloat(argv[2])); a++) {
    for (let a = 0; a < Math.floor(parseFloat(argv[2])); a++) {
      process.stdout.write('X');
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
