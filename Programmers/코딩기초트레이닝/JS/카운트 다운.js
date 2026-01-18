// https://school.programmers.co.kr/learn/courses/30/lessons/181899?language=javascript

// 내 답안
function solution(start_num, end_num) {
    var answer = [];
    var num = start_num;
    for (let i = 0; i < start_num - end_num + 1; i++)
        answer[i] = num--;
    return answer;
}

// 간결하고 깔끔한 답안
const solution = (start, end) => Array(start - end + 1).fill(start).map((v, i) => v - i);