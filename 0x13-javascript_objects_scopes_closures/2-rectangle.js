#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0) {
      return {};
    } else {
      this.width = w;
    }

    if (h <= 0) {
      return {};
    } else {
      this.height = h;
    }
  }
}

module.exports = Rectangle;
