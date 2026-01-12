// https://school.programmers.co.kr/learn/courses/30/lessons/181913?language=javascript

// 내 답안
function solution(my_string, queries) {
    for ([s, e] of queries) {
        my_string = my_string.slice(0, s)
            + my_string.slice(s, e + 1).split("").reverse().join("") // 문자열을 split('')해서 배열로, 뒤집고 join('')으로 다시 문자열로.
            + my_string.slice(e + 1, my_string.length);
    }
    return my_string;
}