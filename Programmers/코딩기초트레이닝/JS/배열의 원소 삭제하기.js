// https://school.programmers.co.kr/learn/courses/30/lessons/181844?language=javascript

function solution(arr, delete_list) {
    return arr.filter((v) => !delete_list.includes(v));
}