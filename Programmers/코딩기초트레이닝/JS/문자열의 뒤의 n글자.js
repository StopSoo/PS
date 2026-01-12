// https://school.programmers.co.kr/learn/courses/30/lessons/181910?language=javascript

// 내 답안
function solution(my_string, n) {
    return my_string.slice(-n);
}
// 다른 답안
function solution(my_string, n) {
    return my_string.substring(my_string.length - n);
}