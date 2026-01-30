// https://school.programmers.co.kr/learn/courses/30/lessons/181847?language=javascript

// 내 답안
// 아이디어: 숫자화 -> 다시 문자열화
function solution(n_str) {
    return String(Number(n_str));
}

// 아이디어 2: replaceAll() 함수를 사용해서 모든 '0'을 ''로 바꾼다.