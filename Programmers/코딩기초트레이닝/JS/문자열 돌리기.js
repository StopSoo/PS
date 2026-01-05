// https://school.programmers.co.kr/learn/courses/30/lessons/181945

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
    input = [line];
}).on("close", function () {
    // 내가 작성한 부분
    str = input[0];
    for (s of str) { // 배열 혹은 문자열에서 of 사용해서 순회 가능
        console.log(s);
    }
});