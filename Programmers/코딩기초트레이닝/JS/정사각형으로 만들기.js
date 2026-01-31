// https://school.programmers.co.kr/learn/courses/30/lessons/181830?language=javascript

function solution(arr) {
    var row = arr.length, col = arr[0].length;
    // 1. map은 원본 배열을 바꾸지 않는다.
    // 2. concat() 함수로 두 배열을 합칠 수 있다.
    if (row > col) {
        arr = arr.map((line) => line.concat(new Array(row - col).fill(0)));
    } else if (row < col) {
        for (let i = 0; i < col - row; i++)
            arr.push(new Array(col).fill(0));
    }
    return arr;
}