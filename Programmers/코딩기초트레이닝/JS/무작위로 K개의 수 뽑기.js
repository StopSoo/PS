// https://school.programmers.co.kr/learn/courses/30/lessons/181858?language=javascript

// 내 답안
// 중복 제거 후 리스트화하기 -> [...new Set(기존 배열)]
function solution(arr, k) {
    var answer = [...new Set(arr)];
    if (answer.length >= k) return answer.slice(0, k);
    else return [...answer, ...new Array(k - answer.length).fill(-1)];
}