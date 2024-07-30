#!/usr/bin/node

const request = require('request');

const epID = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(`${url}${epID}`, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log(JSON.parse(body).title);
});
