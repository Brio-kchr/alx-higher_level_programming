#!/usr/bin/node

class Rectangle {
  // Class that defines a rectangle

  constructor (w, h) {
    if ((w > 1 && h > 1) && (w && h)) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
