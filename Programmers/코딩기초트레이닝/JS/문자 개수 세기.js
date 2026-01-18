// https://school.programmers.co.kr/learn/courses/30/lessons/181902?language=javascript

// 내 답안
// 문자열.charCodeAt(인덱스): 문자열에서 인덱스 위치에 있는 문자의 아스키코드를 반환
function solution(my_string) {
    var answer = Array(52).fill(0); // 52개 원소가 들어있는 배열을 0으로 채움
    for (let i = 0; i < my_string.length; i++) {
        const ascii = my_string.charCodeAt(i);
        if (65 <= ascii && ascii <= 90) // 대문자
            answer[ascii - 65] += 1;
        else // 소문자
            answer[ascii - 97 + 26] += 1;
    }
    return answer;
}