#!/usr/bin/node
const request = require('request');
const fs = require('node:fs');

const apiUrl = process.argv[2];
const textFile = process.argv[3];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  fs.writeFile(textFile, body, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
