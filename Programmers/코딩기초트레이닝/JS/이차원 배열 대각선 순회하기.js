// https://school.programmers.co.kr/learn/courses/30/lessons/181829?language=javascript

function solution(board, k) {
    var answer = 0;
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[0].length; j++) {
            if (i + j <= k) answer += board[i][j];
        }
    }
    return answer;
}