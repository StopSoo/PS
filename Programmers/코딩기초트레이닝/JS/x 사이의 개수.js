// https://school.programmers.co.kr/learn/courses/30/lessons/181867?language=javascript

// 내 답안
function solution(myString) {
    var answer = [];
    var myString = myString.split("x");
    for (let s of myString) {
        answer.push(s.length);
    }
    return answer;
}
// 간결한 답안
function solution(myString) {
    return myString.split("x").map((v) => v.length);
}