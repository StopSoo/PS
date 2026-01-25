// https://school.programmers.co.kr/learn/courses/30/lessons/181866?language=javascript

function solution(myString) {
    return myString
        .split("x")
        .filter((x) => x)
        .sort();
}