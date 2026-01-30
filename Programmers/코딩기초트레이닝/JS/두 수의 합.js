// https://school.programmers.co.kr/learn/courses/30/lessons/181846?language=javascript

// 내 답안
// 자바스크립트에서 Number는 16자리 정도로 숫자 범위에 제한이 있다.
// 따라서 Number 범위를 넘는 숫자에 대해서는 BigInt를 사용한다 (!)
function solution(a, b) {
    return String(BigInt(a) + BigInt(b));
}