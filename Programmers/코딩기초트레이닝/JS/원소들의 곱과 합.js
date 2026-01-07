// https://school.programmers.co.kr/learn/courses/30/lessons/181929?language=javascript

function solution(num_list) {
    let res1 = num_list.reduce((acc, num) => acc * num, 1);
    let res2 = Math.pow(num_list.reduce((acc, num) => acc + num, 0), 2);

    return res1 < res2 ? 1 : 0;
}