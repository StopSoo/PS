// https://school.programmers.co.kr/learn/courses/30/lessons/181833?language=javascript

// 처음 내 답안
// 문제점: fill() 함수에 객체나 배열을 넣기 떄문에 실제 배열을 복사하는 게 아니라 참조를 복사해서 모든 칸에 채워 넣는다.
//       고로 반복문을 돌면 배열의 모든 원소가 1로 변경되기 떄문에 잘못된 코드임.
function solution(n) {
    var answer = new Array(n).fill(new Array(n).fill(0));
    for (let i = 0; i < n; i++) answer[i][i] = 1;
    return answer;
}

// 고친 답안
function solution(n) {
  // n개의 행을 만들고, 각 행마다 새로운 배열을 생성해서 채움
    var answer = Array.from({ length: n }, () => new Array(n).fill(0));
    for (let i = 0; i < n; i++) answer[i][i] = 1;
    return answer;
}