// https://school.programmers.co.kr/learn/courses/30/lessons/181868?language=javascript

// 내 답안
function solution(my_string) {
    var answer = [];
    var word = "";
    for (let i = 0; i < my_string.length; i++) {
        if (my_string[i] === " ") {
            if (word) answer.push(word);
            word = "";
        } else {
            word += my_string[i];
        }
    }
    if (word) answer.push(word);
    return answer;
}
// 간단한 답안
function solution(my_string) {
    return my_string.split(" ").filter((v) => v);
}