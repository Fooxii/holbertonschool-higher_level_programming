#!/usr/bin/node
const firstArg = Number(process.argv[2]);

if (isNaN(firstArg)) {
  console.log('Missing number of occurrences');
} else {
  let x = firstArg;
  while (x > 0) {
    console.log('C is fun');
    x -= 1;
  }
}
