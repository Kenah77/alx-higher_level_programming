#!/usr/bin/node
const req = require('request');
const apiUrl = process.argv[2];

req(apiUrl, function (error, response, body) {
  if (error) {
    return console.log(error);
  } else {
    const content = JSON.parse(body).results;
    console.log(content.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
