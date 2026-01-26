// https://school.programmers.co.kr/learn/courses/30/lessons/181857?language=javascript

// 내 답안
function solution(arr) {
    var pows = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024];
    if (pows.includes(arr.length)) return arr;
    else {
        for (let p of pows)
            if (p > arr.length)
                return [...arr, ...new Array(p - arr.length).fill(0)];
    }
}
// 수학적 사실을 이용한 답안
function solution(arr) {
    const length = arr.length;
    const totalLength = 2 ** Math.ceil(Math.log2(length));
    return [...arr, ...new Array(totalLength - length).fill(0)];
}