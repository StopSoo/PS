// https://school.programmers.co.kr/learn/courses/30/lessons/181885?language=javascript

function solution(todo_list, finished) {
    return todo_list.filter((l, i) => !finished[i]);
}