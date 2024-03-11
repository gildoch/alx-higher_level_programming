#!/usr/bin/node

const { argv } = require('process');
const x = parseInt(argv[2]);

if (x) {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
} else {
  console.log('Missing size');
}
