// https://school.programmers.co.kr/learn/courses/30/lessons/181854?language=javascript

// 내 답안
function solution(arr, n) {
    arr = arr.map((v, i) =>
        arr.length % 2 ? (!(i % 2) ? v + n : v) : i % 2 ? v + n : v,
    );
    return arr;
}
// 위 코드를 좀 더 정리한 답안
// arr.length % 2 !== idx % 2 조건이 포인트
const solution = (arr, n) =>
    arr.map((num, idx) => (arr.length % 2 !== idx % 2 ? num + n : num));