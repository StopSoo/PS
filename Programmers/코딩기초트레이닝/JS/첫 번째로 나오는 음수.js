// https://school.programmers.co.kr/learn/courses/30/lessons/181896?language=javascript

// 내 답안
// 기본적인 코드
function solution(num_list) {
    for (let i = 0; i < num_list.length; i++) {
        if (num_list[i] < 0) return i;
    }
    return -1;
}

// 괜찮은 답안 1
// 자바스크립트의 findIndex() 함수 활용
// 배열 내에서 조건에 맞는 첫 번째 원소를 반환한다.
const solution = (num_list) => num_list.findIndex((v) => v < 0);

// 괜찮은 답안 2
// 자바스크립트의 filter() 함수 활용
// 배열 내에서 조건에 맞는 모든 원소들을 추출할 수 있음.
function solution(num_list) {
    let a = num_list.filter((c) => c < 0);
    return num_list.indexOf(a[0]);
}