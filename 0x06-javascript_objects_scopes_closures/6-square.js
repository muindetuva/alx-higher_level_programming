#!/usr/bin/node
const Sq = require('./5-square.js');

class Square extends Sq {
  charPrint (c) {
    let line;
    if (c === undefined) {
      line = 'X';
      for (let i = 1; i < this.width; i++) {
        line = line + 'X';
      }
    } else {
      line = c;
      for (let i = 1; i < this.width; i++) {
        line = line + c;
      }
    }
    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }
}

module.exports = Square;
