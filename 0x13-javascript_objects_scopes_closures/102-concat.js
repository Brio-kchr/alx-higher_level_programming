#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], (err, data0) => {
  if (err) {
    return;
  }
  fs.readFile(process.argv[3], (err, data1) => {
    if (err) {
      return;
    }
    const out = data0 + data1;
    fs.writeFile(
      process.argv[4],
      out,
      () => {}
    );
  });
});
