// https://school.programmers.co.kr/learn/courses/30/lessons/181949?language=javascript

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
    result = "";

    for (let i = 0; i < str.length; i++) {
        // 문자.toUpperCase(): 대문자로 변경
        // 문자.toLowerCase(): 소문자로 변경
        if (str[i] === str[i].toUpperCase()) result += str[i].toLowerCase();
        else result += str[i].toUpperCase();
    }

    console.log(result);
});