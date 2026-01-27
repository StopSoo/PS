// https://school.programmers.co.kr/learn/courses/30/lessons/181849?language=javascript

function solution(num_str) {
    return num_str.split("").reduce((acc, v) => acc + +v, 0);
}