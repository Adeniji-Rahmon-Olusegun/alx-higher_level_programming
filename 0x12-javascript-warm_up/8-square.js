#!/usr/bin/node

const firstArg = process.argv[2];
const num = parseInt(firstArg);
let counter;

if (!isNaN(num)) {
  for (counter = 1; counter <= num; counter++) {
    console.log('X'.repeat(num));
  }
} else {
  console.log('Missing size');
}
