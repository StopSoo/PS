// https://school.programmers.co.kr/learn/courses/30/lessons/181903?language=javascript

function solution(q, r, code) {
    return [...code].filter((ch, i) => i % q === r).join("");
}