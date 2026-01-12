// https://school.programmers.co.kr/learn/courses/30/lessons/181911?language=javascript

// 내 답안
function solution(my_strings, parts) {
    var answer = [];
    for (let i = 0; i < my_strings.length; i++) {
        answer.push(my_strings[i].slice(parts[i][0], parts[i][1] + 1));
    }
    return answer.join("");
}
// 좀 더 간결한 답안
function solution(my_strings, parts) {
    return parts.map(([s, e], i) => my_strings[i].slice(s, e + 1)).join("");
}
