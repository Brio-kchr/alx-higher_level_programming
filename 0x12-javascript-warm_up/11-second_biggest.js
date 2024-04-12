#!/usr/bin/node

const { argv } = require('node:process');

const a = argv.length;

if (argv.length < 4) {
  console.log(0);
} else {
  const myArr = argv.slice(2, a);
  let b = 0;
  let c = 0;
  myArr.forEach((element) => {
    if (!isNaN(parseFloat(element))) {
      if (Math.floor(parseFloat(element)) >= b) {
        c = b;
        b = Math.floor(parseFloat(element));
      } else if (Math.floor(parseFloat(element)) >= c) {
        c = Math.floor(parseFloat(element));
      }
    }
  });
  console.log(c); // Add this line to print the maximum value found
}
