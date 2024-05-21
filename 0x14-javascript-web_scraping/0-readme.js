#!/usr/bin/node

const fileSys = require('fs');
const fileName = process.argv[2];

fileSys.readFile(fileName, 'utf8', (error, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log(data);
  }
});
