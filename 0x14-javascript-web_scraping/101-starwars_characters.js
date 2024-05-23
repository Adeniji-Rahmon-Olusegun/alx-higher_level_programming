#!/usr/bin/node

const req = require('request');

const movieId = process.argv[2];

const movieApiEndpoint = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

req(movieApiEndpoint, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const films = JSON.parse(body);
    const movieCharacters = films.characters;

    movieCharacters.forEach(movieCharactersUrl => {
      req(movieCharactersUrl, (err, response, body) => {
        if (err) {
          console.error(err);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});
