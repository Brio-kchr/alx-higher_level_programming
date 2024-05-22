#!/usr/bin/node
//  Reads a file and displays its contents

const fs = require('fs');
const fileName = process.argv[2];

fs.readFile(fileName, 'utf8', (err, data) => {
//  if (err) throw err;
  console.log(err || data);
});

// Exit on uncaught errors
//  process.on('uncaughtException', err => {
//    console.error(`Error: ${err}`);
//    process.exit(1);
//  })
