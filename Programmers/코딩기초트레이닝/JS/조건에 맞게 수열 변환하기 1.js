// https://school.programmers.co.kr/learn/courses/30/lessons/181882?language=javascript

// 답안 1
// 기본 작성
function solution(arr) {
    var answer = [];
    for (let e of arr) {
        if (e >= 50 && e % 2 === 0) answer.push(e / 2);
        else if (e < 50 && e % 2 === 1) answer.push(e * 2);
        else answer.push(e);
    }
    return answer;
}

// 답안 2
// map 활용하기
function solution(arr) {
    return arr.map((e, i) =>
        e >= 50 && !(e % 2) ? e / 2 : e < 50 && e % 2 ? e * 2 : e
    );
}