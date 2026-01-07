// https://school.programmers.co.kr/learn/courses/30/lessons/181932?language=javascript

function solution(code) {
    let ret = "";
    let mode = 0;
    for (let i = 0; i < code.length; i++) {
        if (code[i] === "1") mode = (mode + 1) % 2;
        else if (i % 2 === mode) ret += code[i];
    }

    return ret ? ret : "EMPTY";
}