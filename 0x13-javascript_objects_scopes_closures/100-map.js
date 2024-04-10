#!/usr/bin/node

const list = require('./100-data.js');
console.log(list);

const newList = list.map((num, idx) => num * idx);
console.log(newList);
