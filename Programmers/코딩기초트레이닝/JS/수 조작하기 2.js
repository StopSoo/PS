// https://school.programmers.co.kr/learn/courses/30/lessons/181925?language=javascript

// 내 코드
const gaps = {
    "1": "w",
    "-1": "s",
    "10": "d",
    "-10": "a",
};

function solution(numLog) {
    var answer = "";
    for (let i = 1; i < numLog.length; i++) {
        answer += gaps[(numLog[i] - numLog[i - 1]).toString()];
    }
    return answer;
}



// 좀 더 깔끔한 코드
function solution(numLog) {
    const convert = {
        "1": "w",
        "-1": "s",
        "10": "d",
        "-10": "a",
    };

    return numLog.slice(1).map((v, i) => {
        return convert[v - numLog[i]];
    }).join("");
}