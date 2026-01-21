// https://school.programmers.co.kr/learn/courses/30/lessons/181875?language=javascript

function solution(strArr) {
    return strArr.map((e, i) => (i % 2 ? e.toUpperCase() : e.toLowerCase()));
}