// https://school.programmers.co.kr/learn/courses/30/lessons/181871?language=javascript

// 내 답안
// 슬라이딩 윈도우 활용
function solution(myString, pat) {
    var size = pat.length;
    var count = 0;
    for (let i = 0; i < myString.length - size + 1; i++) {
        if (myString.substring(i, i + size) === pat) count++;
    }
    return count;
}
