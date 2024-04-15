#!/usr/bin/node

class Rectangle {
  // Class that defines a rectangle

  constructor (w, h) {
    if ((w > 1 && h > 1) && (w && h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }
}

module.exports = Rectangle;
