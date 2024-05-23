#!/usr/bin/node
//  prints all characters of a Star Wars movie from starwars api

const request = require('request');
const id = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${id}`, function (error, response, body) {
  if (error) {
    console.error('error:', error); // Prints the error if one occurs
  } else if (response) {
    for (const character of JSON.parse(body).characters) {
      request(character, (error, response, body) => {
        if (error) {
          console.log(error);
        } else if (response) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
