// https://school.programmers.co.kr/learn/courses/30/lessons/181935?language=javascript

function solution(n) {
    const isEven = n % 2 === 0;
    const arr = Array.from({ length: n }, (_, i) => i + 1);
    const filter = arr.filter((n) => {
        return isEven ? n % 2 === 0 : n % 2 === 1;
    });
    return isEven
        ? filter.reduce((acc, curr) => acc + curr * curr, 0)
        : filter.reduce((acc, curr) => acc + curr, 0);
}