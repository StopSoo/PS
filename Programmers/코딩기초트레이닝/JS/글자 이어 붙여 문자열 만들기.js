// https://school.programmers.co.kr/learn/courses/30/lessons/181915?language=python3

// 내 답안
function solution(my_string, index_list) {
    var answer = [];
    for (i of index_list) answer.push(my_string[i]);
    return answer.join("");
}
// 더 간결한 답안
function solution(my_string, index_list) {
    return index_list.map((i) => my_string[i]).join("");
}