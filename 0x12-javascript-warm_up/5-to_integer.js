#!/usr/bin/node

const { argv } = require('node:process');

if (argv[2]) {
  if (isNaN(parseFloat(argv[2]))) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + Math.floor(parseFloat(argv[2])));
  }
} else {
  console.log('Not a number');
}
