#!/usr/bin/node

const request = require('request');

request(process.argv[2], (_error, response) => {
  console.log('code:', response && response.statusCode);
});
