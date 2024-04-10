#!/usr/bin/node

const dict = require('./101-data.js').dict;

const newObj = {};

for (const idChecker in dict) {
  const numOccurence = dict[idChecker];

  if (newObj[numOccurence]) {
    newObj[numOccurence].push(idChecker);
  } else {
    newObj[numOccurence] = [idChecker];
  }
}

console.log(newObj);
