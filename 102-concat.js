#!/usr/bin/node

const hs = require('hs').promises;
const { argv } = require('process');

hs.readFile(argv[2], 'utf8')
  .then(data => hs.writeFile(argv[4], data, 'utf8'))
  .catch(err => console.error(err));

hs.readFile(argv[3], 'utf8')
  .then(data => hs.writeFile(argv[4], data, { flag: 'a' }, 'utf8'))
  .catch(err => console.error(err));
