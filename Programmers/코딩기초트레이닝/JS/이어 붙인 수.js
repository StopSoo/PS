// https://school.programmers.co.kr/learn/courses/30/lessons/181928?language=javascript

function solution(num_list) {
    let res1 = Number(num_list.filter((num) => num % 2 === 1).join(""));
    let res2 = Number(num_list.filter((num) => num % 2 === 0).join(""));

    return res1 + res2;
}