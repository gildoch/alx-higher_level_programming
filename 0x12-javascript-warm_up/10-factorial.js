#!/usr/bin/node

const { argv } = require("process");
let x = parseInt(argv[2]);

function fact(x) {
  if (x === 0) return 1;
  return x * fact(x - 1);
}

if (x) console.log(fact(x));
else console.log(1);
