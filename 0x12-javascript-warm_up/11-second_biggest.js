#!/usr/bin/node

const { argv } = require('process');
let numbers;

if (argv.length >= 3) {
  numbers = argv.slice(2).map((number) => parseInt(number)).sort((a, b) => {
    if (a < b) {
      return 1;
    } else {
      return -1;
    }
  });
}

if (argv.length === 2 || argv.length === 3) {
  console.log('0');
} else {
  console.log(
    numbers[1]
  );
}
