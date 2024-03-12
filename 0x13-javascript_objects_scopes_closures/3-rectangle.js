#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print = function () {
    for (let j = 0; j < this.height; j++) {
      console.log('X'.repeat(this.width));
    }
  };
};
