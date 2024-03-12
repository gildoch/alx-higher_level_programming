#!/usr/bin/node

module.exports = class Rectangle {
  constructor (width, height) {
    if (typeof width === 'number' && width > 0 && typeof height === 'number' && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print = function () {
    for (let j = 0; j < this.height; j++) {
      console.log('X'.repeat(this.width));
    }
  };
};
