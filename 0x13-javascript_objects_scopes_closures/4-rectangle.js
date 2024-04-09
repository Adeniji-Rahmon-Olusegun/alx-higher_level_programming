#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;

    for (i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    let j;
    
    for (j = 0; j < this.width; j++) {
      console.log('X'.repeat(this.height));
    }
  }

  double () {
    let k;
   
    for (k = 0; k < (this.width * 2); k++) {
      console.log('X'.repeat(this.height * 2));
    }
  }
}

module.exports = Rectangle;
