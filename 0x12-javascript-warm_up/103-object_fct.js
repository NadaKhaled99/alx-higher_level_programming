#!/usr/bin/node
//adding new function incr that increments integer value
let myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr = function () {
  myObject.value += 1;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
