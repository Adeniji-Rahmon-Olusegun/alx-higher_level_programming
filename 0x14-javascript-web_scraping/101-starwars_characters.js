#!/usr/bin/node

const axios = require('axios');

const movieId = process.argv[2];

const movieApiEndpoint = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

async function orderedCharacters () {
  try {
    const response = await axios.get(movieApiEndpoint);
    const films = response.data;
    const movieCharacterUrls = films.characters;

    for (const url of movieCharacterUrls) {
      const charResponse = await axios.get(url);
      const character = charResponse.data;
      console.log(character.name);
    }
  } catch (error) {
    console.error(error);
  }
}

orderedCharacters();
