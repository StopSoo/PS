// https://school.programmers.co.kr/learn/courses/30/lessons/181918?language=javascript

// 내 답안
function solution(arr) {
    var stk = [];
    let i = 0;
    while (i < arr.length) {
        if (stk.length === 0) {
            stk.push(arr[i++]);
        } else {
            if (stk[stk.length - 1] < arr[i]) {
                stk.push(arr[i++]);
            } else
                stk.pop();
        }
    }
    return stk;
}
