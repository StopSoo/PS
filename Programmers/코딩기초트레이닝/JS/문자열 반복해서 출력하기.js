// https://school.programmers.co.kr/learn/courses/30/lessons/181950

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
    str = input[0];
    n = Number(input[1]);

    console.log(str.repeat(n)); // 문자열.repeat(횟수)
});