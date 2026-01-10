// https://school.programmers.co.kr/learn/courses/30/lessons/181919?language=javascript

// 내 답안 (기본적)
function solution(n) {
    var answer = [n];
    while (true) {
        if (n === 1) break;

        if (n % 2 == 0) n /= 2;
        else n = 3 * n + 1;
        answer.push(n);
    }
    return answer;
}

// 재귀 함수를 사용한 답안
function solution(n, arr = []) {
    arr.push(n);
    if (n === 1) return arr;
    if (n % 2 === 0) return solution(n / 2, arr);
    return solution(3 * n + 1, arr);
}