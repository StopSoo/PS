// https://school.programmers.co.kr/learn/courses/30/lessons/181901?language=javascript

// 내 답안
function solution(n, k) {
    var answer = [];
    for (let i = k; i <= n; i += k)
        answer.push(i);
    return answer;
}