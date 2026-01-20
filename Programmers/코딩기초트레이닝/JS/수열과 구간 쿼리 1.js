// https://school.programmers.co.kr/learn/courses/30/lessons/181883?language=javascript

function solution(arr, queries) {
    for (let [s, e] of queries) { // of를 쓰는 거 헷갈리지 말기 !!!
        for (let i = s; i <= e; i++)
            arr[i] += 1;
    }
    return arr;
}