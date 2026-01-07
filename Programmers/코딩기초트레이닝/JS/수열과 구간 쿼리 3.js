// https://school.programmers.co.kr/learn/courses/30/lessons/181924?language=javascript

function solution(arr, queries) {
    for ([a, b] of queries) {
        [arr[a], arr[b]] = [arr[b], arr[a]]; // 구조 분해 할당 사용하기
    }
    return arr;
}