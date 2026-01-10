// https://school.programmers.co.kr/learn/courses/30/lessons/181921?language=javascript

function solution(l, r) {
    var answer = [];
    for (let num = l; num <= r; num++) {
        if (num.toString().replaceAll("0", "").replaceAll("5", "") === "")
            answer.push(num);
    }
    return answer.length > 0 ? answer : [-1];
}