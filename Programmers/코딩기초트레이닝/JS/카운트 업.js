// https://school.programmers.co.kr/learn/courses/30/lessons/181920?language=javascript

// 내 답안
function solution(start_num, end_num) {
    var arr = [];
    for (let i = start_num; i <= end_num; i++) arr.push(i);
    return arr;
}

// 간결하고 깔끔한 답안 1
function solution(start, end) {
    return Array.from({ length: end - start + 1 }, () => { return start++; });
}

// 간결하고 깔끔한 답안 2
function solution(start, end) {
    return Array(end - start + 1)
        .fill(start)
        .map((x, idx) => x + idx);
}