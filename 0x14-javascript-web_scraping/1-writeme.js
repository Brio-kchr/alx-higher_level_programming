#!/usr/bin/node
//  Writes data to a file

const fs = require('fs');
const fileName = process.argv[2];

fs.writeFile(fileName, process.argv[3], (err) => {
  if (err) {
    console.log(err);
  }
});

// Exit on uncaught errors
//  process.on('uncaughtException', err => {
//    console.error(`Error: ${err}`);
//    process.exit(1);
//  })
