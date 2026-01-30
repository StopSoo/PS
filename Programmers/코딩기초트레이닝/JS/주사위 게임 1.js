// https://school.programmers.co.kr/learn/courses/30/lessons/181839?language=javascript

// 내 답안
function solution(a, b) {
    if ([a, b].every((num) => num % 2 === 1)) return a ** 2 + b ** 2;
    else if ([a, b].some((num) => num % 2 === 1)) return 2 * (a + b);
    else return Math.abs(a - b);
}
// 좀 더 간결하고 함수를 사용한 답안
// 삼항 연산자를 사용한 것도 포인트 ~!
function solution(a, b) {
    const isOdd = (num) => num % 2 === 1;

    return isOdd(a) && isOdd(b)
        ? a ** 2 + b ** 2
        : isOdd(a) || isOdd(b)
        ? 2 * (a + b)
        : Math.abs(a - b);
}