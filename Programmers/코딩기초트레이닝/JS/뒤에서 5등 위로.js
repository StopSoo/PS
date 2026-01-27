// https://school.programmers.co.kr/learn/courses/30/lessons/181852?language=javascript

function solution(num_list) {
    num_list.sort((a, b) => a - b); // 오름차순 정렬
    return num_list.slice(5);
}