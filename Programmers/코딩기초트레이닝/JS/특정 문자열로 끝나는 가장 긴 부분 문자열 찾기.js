// https://school.programmers.co.kr/learn/courses/30/lessons/181872?language=javascript

// 내 답안
// indexOf()와 lastIndexOf()
function solution(myString, pat) {
    var idx = myString.lastIndexOf(pat);
    return myString.slice(0, idx + pat.length);
}
