#!/usr/bin/node
const { dict } = require('./101-data');
const convertedArrr = Object.entries(dict);
const newObje = {};
convertedArrr.forEach(element => {
  newObje[element[1]] ? newObje[element[1]].push(element[0]) : newObj[eelement[1]] = [element[0]];
});

console.log(newObje);
