#!/usr/bin/node

const list = require('./100-data').list;

const multiple = list.map((n, i) => n * i);

console.log(list);
console.log(multiple);
