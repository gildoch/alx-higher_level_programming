#!/usr/bin/node

const axios = require('axios');

const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
const filmId = process.argv[2];

const getCharDetails = async (url) => {
  try {
    const response = await axios.get(url);
    console.log(response.data.name);
  } catch (error) {
    console.log(error);
  }
};

const getFilmDetails = async (url) => {
  try {
    const response = await axios.get(url);
    const characters = response.data.characters;
    for (const char of characters) {
      await getCharDetails(char);
    }
  } catch (error) {
    console.log(error);
  }
};

getFilmDetails(`${apiUrl}${filmId}`);
