// https://school.programmers.co.kr/learn/courses/30/lessons/181891?language=javascript

// 내 답안
// slice()는 본 배열을 변경시키지 않는다.
function solution(num_list, n) {
    return [...num_list.slice(n), ...num_list.slice(0, n)];
}