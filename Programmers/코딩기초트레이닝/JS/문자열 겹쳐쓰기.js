// https://school.programmers.co.kr/learn/courses/30/lessons/181943?language=javascript

function solution(my_string, overwrite_string, s) {
    var answer = "";
    // 문자열.slice(시작 인덱스, 종료 인덱스 + 1): 문자열의 시작 인덱스부터 종료 인덱스까지 slicing
    // 문자열.slice(인덱스): 문자열의 인덱스부터 마지막까지 slicing
    answer = my_string.slice(0, s) + overwrite_string + my_string.slice(s + overwrite_string.length);
    return answer;
}