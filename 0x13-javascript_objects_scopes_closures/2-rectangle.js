#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0) {
      this.w = undefined;
    } else {
      this.width = w;
    }

    if (h <= 0) {
      this.h = undefined;
    } else {
      this.height = h;
    }
  }
}

module.exports = Rectangle;
