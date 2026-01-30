// https://school.programmers.co.kr/learn/courses/30/lessons/181841?language=javascript

function solution(str_list, ex) {
    return str_list.filter((v) => !v.includes(ex)).join("");
}