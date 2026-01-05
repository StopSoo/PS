// https://school.programmers.co.kr/learn/courses/30/lessons/181946

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
    input = line.split(" ");
}).on("close", function () {
    // 내가 작성한 부분
    str1 = input[0];
    str2 = input[1];
    console.log(input[0] + input[1]);
});