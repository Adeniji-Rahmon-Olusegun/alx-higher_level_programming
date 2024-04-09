#!/usr/bin/node

const Rectangle = require('./5-square');

class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    let i;

    for (i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
