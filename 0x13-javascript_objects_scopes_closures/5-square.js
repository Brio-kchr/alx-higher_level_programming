#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  // Class that defines a rectangle

  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
