// https://school.programmers.co.kr/learn/courses/30/lessons/181909

function solution(my_string) {
    var answer = [];
    for (let i = 0; i < my_string.length; i++) {
        answer.push(my_string.slice(i));
    }
    answer.sort(); // 사전 순 정렬
    return answer;
}