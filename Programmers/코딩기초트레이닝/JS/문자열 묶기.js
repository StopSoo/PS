// https://school.programmers.co.kr/learn/courses/30/lessons/181855?language=javascript

// 내 답안
// 1. max 함수의 인자는 spread 형태로 들어가야 한다. (파이썬과 다름)
// 2. Object.keys(객체명) / Object,values(객체명) 형태로 사용하기
function solution(strArr) {
    var dt = {};
    for (let s of strArr) {
        dt[s.length] = (dt[s.length] || 0) + 1;
    }
    return Math.max(...Object.values(dt));
}
// Map을 사용한 답안
// Map도 잘 알아놓자 !! -> set 함수와 get 함수, 그리고 values() 
function solution(strArr) {
    const counter = new Map();
    for (const str of strArr) {
        counter.set(str.length, (counter.get(str.length) || 0) + 1);
    }
    return Math.max(...counter.values());
}