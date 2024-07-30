#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  body = JSON.parse(body).results;
  const charCount = body.map(char => char.characters).flat().filter(char => char.includes(18)).length;
  console.log(charCount);
});
