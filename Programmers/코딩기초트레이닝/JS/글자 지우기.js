// https://school.programmers.co.kr/learn/courses/30/lessons/181900?language=javascript

// 내 답안
// 배열.includes(값): 배열에 값이 포함되어 있는지 유무를 반환
// not은 !로 표현
function solution(my_string, indices) {
    var answer = [];
    for (let i = 0; i < my_string.length; i++) {
        if (!indices.includes(i))
            answer.push(my_string[i]);
    }
    return answer.join("");
}