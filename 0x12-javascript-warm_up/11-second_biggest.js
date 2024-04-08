#!/usr/bin/node

const argLen = (process.argv.length);
const intList = [];
let counter = 0;

if (argLen < 3) {
  console.log(0);
} else if (argLen === 3) {
  console.log(0);
} else {
  for (counter = 2; counter < argLen; counter++) {
    intList.push(process.argv[counter]);
  }

  intList.sort((a, b) => b - a);

  console.log(intList[1]);
}
