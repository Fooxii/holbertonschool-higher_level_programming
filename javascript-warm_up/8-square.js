#!/usr/bin/node
const size = Number(process.argv[2]);

if (isNaN(size) || size <= 0) {
  console.log('Missing size');
} else {
  // This for loop prints row and repeats
  for (let i = 0; i < size; i++) {
    let row = '';
    // This for loop adds 'X' size times
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
