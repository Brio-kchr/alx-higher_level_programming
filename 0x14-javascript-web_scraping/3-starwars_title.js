#!/usr/bin/node
//  prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');
const id = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${id}`, function (error, response, body) {
  if (error) {
    console.error('error:', error); // Prints the error if one occurs
  } else if (response) {
    console.log(JSON.parse(response.body).title);
  }
});
