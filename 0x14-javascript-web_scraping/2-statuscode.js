#!/usr/bin/node

const req = require('request');

const url = process.argv[2];

req(url, (err, response) => {
  if (err) {
    console.error(err);
  } else {
    console.log('code:', response.statusCode);
  }
});
