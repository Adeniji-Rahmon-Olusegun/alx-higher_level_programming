#!/usr/bin/node

const firstArg = process.argv[2];
const num = parseInt(firstArg);
let counter = 1;

if (!isNaN(num)) {
  while (counter <= num) {
    console.log('C is fun');
    counter++;
  }
} else {
  console.log('Missing number of occurences');
}
