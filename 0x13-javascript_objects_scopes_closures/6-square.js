#!/usr/bin/node

const Square1 = require('./5-square');

class Square extends Square1 {
  // Class that defines a rectangle

  constructor (size) {
    super(size);
  }

  charPrint (C) {
    console.log(C)
    if (typeof (C) !== 'undefined') {
      console.log(C, super.size)
      for (let i = 0; i < super.size; i++) {
        for (let j = 0; j < super.size; j++) {
          process.stdout.write(C);
        }
        console.log();
      }
    } else {
      super.super.print()
    }
  }
}

module.exports = Square;
