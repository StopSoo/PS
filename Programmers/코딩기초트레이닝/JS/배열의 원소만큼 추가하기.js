// https://school.programmers.co.kr/learn/courses/30/lessons/181861?language=javascript

// 내 답안 (기본적 코드)
function solution(arr) {
    var X = [];
    for (let e of arr) {
        for (let i = 0; i < e; i++) X.push(e);
    }
    return X;
}
// 간결하고 깔끔한 답안
function solution(arr) {
    return arr.reduce((list, num) => [...list, ...new Array(num).fill(num)], []);
}