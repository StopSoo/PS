// https://school.programmers.co.kr/learn/courses/30/lessons/181865?language=javascript

// 내 답안
function solution(binomial) {
    var arr = binomial.split(" ");
    if (arr[1] === "+") return Number(arr[0]) + Number(arr[2]);
    else if (arr[1] === "-") return Number(arr[0]) - Number(arr[2]);
    else return Number(arr[0]) * Number(arr[2]);
}
// 멋진 답안
const ops = {
    "+": (a, b) => a + b,
    "-": (a, b) => a - b,
    "*": (a, b) => a * b,
};

function solution(binomial) {
    const [a, op, b] = binomial.split(" "); // 구조 분해 할당
    return ops[op](+a, +b); // +는 숫자로 변환
}