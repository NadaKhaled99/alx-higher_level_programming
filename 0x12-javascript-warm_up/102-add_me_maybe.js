#!/usr/bin/node
//function that increments and calls another function
exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
