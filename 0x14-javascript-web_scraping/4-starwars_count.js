#!/usr/bin/node

const request = require('request');
const starWarsUri = process.argv[2];
let times = 0;
request(starWarsUri, function (_err, _res, body) {
  body = JSON.parse(body).results;

  for (let n = 0; n < body.length; ++n) {
    const characters = body[n].characters;

    for (let m = 0; m < characters.length; ++m) {
      const character = characters[m];
      const characterId = character.split('/')[5];

      if (characterId === '18') {
        times += 1;
      }
    }
  }

  console.log(times);
});
