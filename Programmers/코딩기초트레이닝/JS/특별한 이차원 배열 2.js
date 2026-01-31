// https://school.programmers.co.kr/learn/courses/30/lessons/181831?language=javascript

// 내 답안
// 조건에 걸리면 return으로 이중 for문 나오기
function solution(arr) {
    var n = arr.length;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (arr[i][j] != arr[j][i]) return 0;
        }
    }
    return 1;
}