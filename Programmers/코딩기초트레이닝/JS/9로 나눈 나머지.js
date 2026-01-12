// https://school.programmers.co.kr/learn/courses/30/lessons/181914?language=javascript

function solution(number) {
    return [...number].reduce((acc, num) => acc + Number(num), 0) % 9;
}