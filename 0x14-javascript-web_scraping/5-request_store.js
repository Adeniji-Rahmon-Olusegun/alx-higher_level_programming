#!/usr/bin/node

const req = require('request');
const fileSys = require('fs');

const url = process.argv[2];
const fileName = process.argv[3];

req(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    fileSys.writeFile(fileName, body, 'utf8', (error) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
