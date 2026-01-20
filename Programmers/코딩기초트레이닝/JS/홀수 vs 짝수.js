// https://school.programmers.co.kr/learn/courses/30/lessons/181887?language=javascript

function solution(num_list) {
    var sum_odd = 0;
    var sum_even = 0;
    for (let i = 0; i < num_list.length; i++) {
        if ((i + 1) % 2 == 0) sum_odd += num_list[i];
        else sum_even += num_list[i];
    }
    return sum_odd > sum_even ? sum_odd : sum_even;
}