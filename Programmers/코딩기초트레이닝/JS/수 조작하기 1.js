// https://school.programmers.co.kr/learn/courses/30/lessons/181926?language=javascript

// 내 답안
function solution(n, control) {
    for (ch of control) {
        ch === "w"
            ? (n += 1)
            : ch === "s"
                ? (n -= 1)
                : ch === "d"
                    ? (n += 10)
                    : (n -= 10);
    }
    return n;
}

// 깔끔한 코드
const operations = {
    w: (n) => n + 1,
    s: (n) => n - 1,
    d: (n) => n + 10,
    a: (n) => n - 10,
};

function solution(n, control) {
    return [...control].reduce((prev, op) => operations[op](prev), n);
}