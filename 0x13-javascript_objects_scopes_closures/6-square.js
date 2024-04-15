#!/usr/bin/node

const Square1 = require('./5-square');

class Square extends Square1 {
  // Class that defines a square that extendes a square

  charPrint (C = 'X') {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(C);
      }
      console.log();
    }
  }
}

module.exports = Square;
