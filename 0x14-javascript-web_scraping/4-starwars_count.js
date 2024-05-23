#!/usr/bin/node
//  prints the number of movies where the character “Wedge Antilles” is present

const request = require('request');
const url = process.argv[2];

request(url, function (error, response) {
  if (error) {
    console.error('error:', error); // Prints the error if one occurs
  } else if (response) {
    const resultsList = JSON.parse(response.body).results;
    let count = 0;
    resultsList.forEach((element) => {
      const list = element.characters;
      list.forEach((element) => {
        if (element.slice(-3) === '18/') {
          count++;
        }
      });
    });
    console.log(count);
  }
});
