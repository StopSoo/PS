// https://school.programmers.co.kr/learn/courses/30/lessons/181880?language=javascript

// 내 답안
// 정직한 로직으로 작성
function solution(num_list) {
    var answer = 0;
    for (let number of num_list) {
        while (number != 1) {
            if (number % 2 == 0) number /= 2;
            else number = (number - 1) / 2;
            answer += 1;
        }
    }
    return answer;
}
// 다른 사람의 답안
// 1이 되기까지 나누는 횟수를 계산하는 방식 = 숫자를 2진수로 만들고 그 자릿수에서 1을 뺀다.
// 숫자.toString(진법) 문법으로 숫자의 진법을 변경할 수 있다.
function solution(num_list) {
    return num_list.map((v) => v.toString(2).length - 1).reduce((a, c) => a + c);
}