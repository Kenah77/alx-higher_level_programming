#!/usr/bin/node

const req = require('request');
const movieId = process.argv[2];
const api = 'https://swapi-api.hbtn.io/api/films/' + movieId;

req(api, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  console.log(JSON.parse(body).title);
});
