#!/usr/bin/node

exports.esrever = function (list) {
  let a = list.length;
  const revList = [];
  list.forEach((element) => {
    revList[--a] = element;
  });
  return revList;
};
