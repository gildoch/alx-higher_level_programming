#!/usr/bin/node

const dict = require('./101-data');
const newDict = {};
Object.entries(dict).forEach(([key, value]) => {
  if (!Array.isArray(newDict[value])) {
    newDict[value] = [];
  }
  newDict[value].push(key);
});

console.log(newDict);
