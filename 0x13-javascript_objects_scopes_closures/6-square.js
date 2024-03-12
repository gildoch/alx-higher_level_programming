#!/usr/bin/node

const SquareB = require('./5-square');
module.exports = class Square extends SquareB {
  charPrint = function (c) {
    if (c) {
      for (let i = 0; i < this.size; i++) {
        console.log(c.repeat(this.size));
      }
    } else {
      this.print();
    }
  };
};
