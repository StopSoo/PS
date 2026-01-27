// https://school.programmers.co.kr/learn/courses/30/lessons/181851?language=javascript

function solution(rank, attendance) {
    var values = [];
    for (let r = 1; r <= rank.length; r++) {
        if (values.length === 3) break;
        if (attendance[rank.indexOf(r)]) values.push(rank.indexOf(r));
    }
    return 10000 * values[0] + 100 * values[1] + values[2];
}