// https://school.programmers.co.kr/learn/courses/30/lessons/181874?language=javascript

// 내 답안
// 문자열은 map 못 씀 ~ split('')으로 배열화하기 !!
function solution(myString) {
    return myString.split("")
        .map((e, i) => (e === "a" || e === "A" ? "A" : e.toLowerCase())).join("");
}
// 간결한 답안
const solution = (s) => s.toLowerCase().replaceAll("a", "A");