#!/usr/bin/node

const list = require('./100-data.js');

const newList = list.map((num, idx) => num * idx);

console.log(list);
console.log(newList);
