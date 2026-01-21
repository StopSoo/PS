// https://school.programmers.co.kr/learn/courses/30/lessons/181878?language=javascript

// 내 답안
// 대소문자를 구분하지 않고 포함 여부를 체크하는 것이므로 
// 비교하려는 문자열과 체크해야 하는 문자열 둘 다 toUpperCase() or toLowerCase() 처리하기 (!)
function solution(myString, pat) {
    return myString.toUpperCase().includes(pat.toUpperCase()) ? 1 : 0;
}