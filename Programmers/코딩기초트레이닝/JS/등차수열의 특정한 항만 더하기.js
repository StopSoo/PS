// https://school.programmers.co.kr/learn/courses/30/lessons/181931?language=javascript

// 내 답안
// 그냥 정석대로 ...
function solution(a, d, included) {
    var answer = 0;
    for (let i = 0; i < included.length; i++) {
        if (included[i]) answer += a + d * i;
    }
    return answer;
}

// 좀 더 간단하고 자스스러운 버전
function solution(a, d, included) {
    return included.reduce((acc, flag, i) => {
        return flag ? acc + a + d * i : acc;
    }, 0);
}