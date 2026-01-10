// https://school.programmers.co.kr/learn/courses/30/lessons/181922

function solution(arr, queries) {
    for ([s, e, k] of queries) {
        for (let i = s; i <= e; i++) {
            if (i % k == 0) arr[i]++;
        }
    }

    return arr;
}