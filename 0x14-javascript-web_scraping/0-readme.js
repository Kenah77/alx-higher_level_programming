#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', (error, data) => {
  if (error) {
    return console.log(error);
  }
  process.stdout.write(data);
}
);
