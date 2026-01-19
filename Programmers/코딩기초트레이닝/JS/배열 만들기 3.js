// https://school.programmers.co.kr/learn/courses/30/lessons/181895?language=javascript

// 내 답안
// 배열의 요소 값을 순회하기 위해서는 for...of를 사용해야 한다 (!)
// 배열의 요소들을 새로운 배열에 넣을 때 push()에 spread해서 넣기 (!)
function solution(arr, intervals) {
    var answer = [];
    for (let [a, b] of intervals) {
        answer.push(...arr.slice(a, b + 1));
    }
    return answer;
}

// 다른 답안
// intervals 길이가 지정되어 있으므로 아예 구조 분해 할당해서 변수에 담아놓고 사용하는 것도 good!
function solution(arr, intervals) {
    const [[a, b], [c, d]] = intervals;

    return [...arr.slice(a, b + 1), ...arr.slice(c, d + 1)];
}