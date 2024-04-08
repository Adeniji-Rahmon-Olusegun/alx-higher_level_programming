#!/usr/bin/node

const firstArg = parseInt(process.argv[2]);

function Factorial (n) {
  if (isNaN(n)) {
    return (1);
  } else if (n === 0) {
    return (1);
  } else {
    return (Factorial(n - 1) * n);
  }
}

console.log(Factorial(firstArg));
