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

  rotate = function () {
    const tmpH = this.height;
    this.height = this.width;
    this.width = tmpH;
  };

  double = function () {
    this.width *= 2;
    this.height *= 2;
  };
};
