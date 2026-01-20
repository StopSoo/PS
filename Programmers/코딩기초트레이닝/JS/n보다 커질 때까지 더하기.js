// https://school.programmers.co.kr/learn/courses/30/lessons/181884?language=javascript

function solution(numbers, n) {
    var answer = 0;
    for (let number of numbers) {
        answer += number;
        if (answer > n) break;
    }
    return answer;
}