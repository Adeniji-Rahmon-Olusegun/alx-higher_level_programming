#!/usr/bin/node

const req = require('request');

const apiEndpoint = process.argv[2];

const charId = '18';

req(apiEndpoint, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const films = JSON.parse(body).results;
    const filmsWithWedge = films.filter(film =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${charId}/`)).length;
    console.log(filmsWithWedge);
  }
});
