// https://school.programmers.co.kr/learn/courses/30/lessons/181912?language=javascript

// 내 답안
function solution(intStrs, k, s, l) {
    var answer = [];
    for (const num of intStrs) {
        const target = Number(num.split("").splice(s, l).join(""));
        if (target > k) answer.push(target);
    }
    return answer;
}
// 간결한 코드
function solution(intStrs, k, s, l) {
    return intStrs.map((v) => +v.slice(s, s + l)).filter((v) => v > k);
}
