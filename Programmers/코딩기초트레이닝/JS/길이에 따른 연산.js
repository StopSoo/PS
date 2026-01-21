// https://school.programmers.co.kr/learn/courses/30/lessons/181879?language=javascript

// 내 답안
// reduce 안에서 조건 분기를 할 수도 있음
function solution(num_list) {
    var s = num_list.reduce((acc, ele) => acc + ele, 0);
    var p = num_list.reduce((acc, ele) => acc * ele, 1);
    return num_list.length >= 11 ? s : p;
}