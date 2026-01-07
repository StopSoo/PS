// https://school.programmers.co.kr/learn/courses/30/lessons/181923?language=javascript

// 내 답안
// 내가 놓쳤던 부분은 sort() 함수
// sort()만 쓴다고 정렬되는 게 아니라 그 안에 기준을 기재해야 한다 (!!!!!)
function solution(arr, queries) {
    var answer = [];
    for ([s, e, k] of queries) {
        let new_arr = arr.slice(s, e + 1).filter((el) => el > k).sort((a, b) => a - b);
        answer.push(new_arr.length > 0 ? new_arr[0] : -1);
    }
    return answer;
}
// 좀 더 간결한 답안
function solution(arr, queries) {
    return queries.map(
        ([s, e, k]) =>
        arr.slice(s, e + 1).filter((n) => n > k).sort((a, b) => a - b)[0] || -1
    );
}