#!/usr/bin/node

const req = require('request');

const movieId = process.argv[2];

const apiEndpoint = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

req(apiEndpoint, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
