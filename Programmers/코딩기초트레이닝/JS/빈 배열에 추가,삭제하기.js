// https://school.programmers.co.kr/learn/courses/30/lessons/181860?language=javascript

// 내 답안
function solution(arr, flag) {
    var X = [];
    for (let i = 0; i < arr.length; i++) {
        if (flag[i])
            X = [...X, ...new Array(arr[i] * 2).fill(arr[i])];
        else
            X = X.slice(0, X.length - arr[i]);
    }
    return X;
}
// reduce를 활용한 답안
function solution(arr, flag) {
    return arr.reduce((prev, num, i) => flag[i] ? [...prev, ...new Array(num * 2).fill(num)] : prev.slice(0, -num), []);
}