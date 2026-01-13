// https://school.programmers.co.kr/learn/courses/30/lessons/181904?language=javascript

// 내 답안
// 하지만 예전에 풀었던 파이썬 코드의 도움을 받음 !!
function solution(my_string, m, c) {
    let answer = "";
    for (let i = 0; i < my_string.length / m; i++) {
        answer += my_string.slice(m * i, m * (i + 1) + 1)[c - 1];
    }
    return answer;
}
// 좀 더 직관적인 답안
function solution(my_string, m, c) {
    let answer = "";
    for (let i = c - 1; i < my_string.length; i += m)
        answer += my_string[i];
    return answer;
}
// 간결하고 깔끔한 답안
// 처음에는 이렇게 풀었으나 i % m === c - 1 조건을 놓치고 다른 조건을 기재했었음.
function solution(my_string, m, c) {
    return [...my_string].filter((_, i) => i % m === c - 1).join("");
}