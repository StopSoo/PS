// https://school.programmers.co.kr/learn/courses/30/lessons/181859?language=javascript

// 내 답안
function solution(arr) {
    var stk = [];
    var i = 0;
    while (i < arr.length) {
        if (stk.length === 0) stk.push(arr[i++]);
        else {
            if (stk[stk.length - 1] === arr[i]) {
                stk.splice(stk.length - 1, 1); // stk.splice(-1); or stk.pop(); 도 가능하다 (!)
                i++;
            } else {
                stk.push(arr[i++]);
            }
        }
    }
    return stk.length > 0 ? stk : [-1];
}