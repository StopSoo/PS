// https://school.programmers.co.kr/learn/courses/30/lessons/181898?language=javascript

// 내 답안
// 맞추긴 했는데 문제가 이상함
function solution(arr, idx) {
    for (let i = idx; i < arr.length; i++) {
        if (arr[i] === 1) return i;
    }
    return -1;
}