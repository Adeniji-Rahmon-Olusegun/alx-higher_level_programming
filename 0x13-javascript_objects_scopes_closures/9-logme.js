#!/usr/bin/node

exports.logMe = function (item) {
  let index = 0;
  const argPos = 2;

  console.log(`${index}: ${process.argv[argPos]}`);

  index++;
};
