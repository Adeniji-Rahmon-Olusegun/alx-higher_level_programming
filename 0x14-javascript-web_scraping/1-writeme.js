#!/usr/bin/node

const fileSys = require('fs');

const fileName = process.argv[2];
const data = process.argv[3];

fileSys.writeFile(fileName, data, 'utf8', (error) => {
  if (error) {
    console.error(error);
  }
});
