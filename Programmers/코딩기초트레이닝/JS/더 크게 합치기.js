// https://school.programmers.co.kr/learn/courses/30/lessons/181939?language=javascript

// 내 답안
function solution(a, b) {
    return Math.max(
        parseInt(a.toString() + b.toString()),
        parseInt(b.toString() + a.toString())
    );
}

// 좋은 답안 1
// - 백틱을 사용해 변수값을 사용할 수 있다는 것
// - parseInt() 대용으로 Number() 함수도 사용할 수 있다는 것 
function solution(a, b) {
    return Math.max(Number(`${a}${b}`), Number(`${b}${a}`));
}

// 좋은 답안 2
// 내 답안과 거의 비슷하나, 문자열을 숫자로 변경할 때 +를 사용함!!
function solution(a, b) {
    return Math.max(
        +(a.toString() + b.toString()),
        +(b.toString() + a.toString())
    );
}