// https://school.programmers.co.kr/learn/courses/30/lessons/181893?language=javascript

// 내 답안
function solution(arr, query) {
    for (let i = 0; i < query.length; i++) {
        if (i % 2 == 0) arr = arr.slice(0, query[i] + 1);
        else arr = arr.slice(query[i]);
    }
    return arr;
}