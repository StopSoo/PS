// https://school.programmers.co.kr/learn/courses/30/lessons/181886?language=javascript

// 간결한 답안
function solution(names) {
    return names.filter((v, i) => i % 5 === 0);
}

// 기본적인 답안
// 전체를 순회하지 않으므로 효율적
function solution(names) {
    var answer = [];
    for (let i = 0; i < names.length; i += 5) {
        answer.push(names[i]);
    }
    return answer;
}