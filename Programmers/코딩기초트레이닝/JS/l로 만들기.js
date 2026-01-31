// https://school.programmers.co.kr/learn/courses/30/lessons/181834?language=javascript

// 내 답안
function solution(myString) {
    return myString.split("").map((v) => (v < "l" ? "l" : v)).join("");
}
// 정규식을 사용한 답안
const solution = (myString) => myString.replace(/[a-k]/g, "l");