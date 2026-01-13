// https://school.programmers.co.kr/learn/courses/30/lessons/181906?language=javascript

// 내 답변
function solution(my_string, is_prefix) {
    return my_string.startsWith(is_prefix) ? 1 : 0;
}
// 간결한 답변
// + 표시는 Number()와 같음
function solution(my_string, is_prefix) {
    return +my_string.startsWith(is_prefix);
}