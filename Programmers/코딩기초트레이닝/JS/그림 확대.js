// https://school.programmers.co.kr/learn/courses/30/lessons/181836?language=javascript

// 내 답안
// 문자열.repeat(반복 횟수)
function solution(picture, k) {
    var answer = [];
    for (let p of picture) {
        for (let i = 0; i < k; i++)
            answer.push(p.split("").map((v) => v.repeat(k)).join(""));
    }
    return answer;
}