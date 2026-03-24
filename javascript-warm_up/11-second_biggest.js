#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = [];
  for (let i = 2; i < process.argv.length; i++) {
    list.push(Number(process.argv[i]));
  }
  let biggest = -Infinity;
  let second = -Infinity;

  for (let i = 0; i < list.length; i++) {
    if (list[i] > biggest) {
      second = biggest;
      biggest = list[i];
    } else if (list[i] > second && list[i] !== biggest) {
      second = list[i];
    }
  }
  console.log(second);
}
