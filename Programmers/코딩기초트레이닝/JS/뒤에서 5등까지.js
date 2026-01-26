// https://school.programmers.co.kr/learn/courses/30/lessons/181853?language=javascript

// 내 답안
// 1. 정렬 기준 적기 -> 오름차순은 a - b
function solution(num_list) {
    num_list.sort((a, b) => a - b); // 오름차순 정렬
    return num_list.slice(0, 5);
}