#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let a = 0;
  list.forEach((element) => {
    if (element === searchElement) {
      a++;
    }
  });
  return a;
};
