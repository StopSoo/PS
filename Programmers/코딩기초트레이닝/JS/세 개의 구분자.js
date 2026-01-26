// https://school.programmers.co.kr/learn/courses/30/lessons/181862?language=javascript

// 내 답안 -> 풀다가 막힘

// 답안 1
function solution(myStr) {
    const tmp1 = myStr.split("a").join("b");
    const tmp2 = tmp1.split("b").join("c");
    const tmp3 = tmp2.split("c").filter((x) => x);
    if (tmp3.length === 0) return ["EMPTY"];
    return tmp3;
}
// 답안 2
function solution(myStr) {
    const list = myStr.split(/[a|b|c]/).filter((str) => str); // a, b, c 중 하나라도 만나면 문자열을 쪼개라.
    return list.length ? list : ["EMPTY"];
}