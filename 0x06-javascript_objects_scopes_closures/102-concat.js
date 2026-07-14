#!/usr/bin/node

const fs = require('fs');

const firstFile = process.argv[2];
const secondFile = process.argv[3];
const destination = process.argv[4];

const firstContent = fs.readFileSync(firstFile, 'utf8');
const secondContent = fs.readFileSync(secondFile, 'utf8');

fs.writeFileSync(destination, firstContent + secondContent);
