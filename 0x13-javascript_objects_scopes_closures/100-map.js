#!/usr/bin/nodes

const list = require('./100-data');

const newList = list.map((num, idx) => num * idx);

console.log(list);
console.log(newList);
