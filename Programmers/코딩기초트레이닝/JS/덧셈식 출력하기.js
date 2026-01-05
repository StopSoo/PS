// https://school.programmers.co.kr/learn/courses/30/lessons/181947

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
    console.log(input[0], "+", input[1], "=", Number(input[0]) + Number(input[1]));
});