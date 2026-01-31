// https://school.programmers.co.kr/learn/courses/30/lessons/181837?language=javascript

// 내 답안
function solution(order) {
    var answer = 0;
    for (let menu of order) {
        if (menu.includes("americano") || menu === "anything") answer += 4500;
        else if (menu.includes("cafelatte")) answer += 5000;
    }
    return answer;
}
// 좀 더 간결한 답안
const solution = (order) => order.reduce((acc, cur) => acc + (cur.includes("latte") ? 5000 : 4500), 0);