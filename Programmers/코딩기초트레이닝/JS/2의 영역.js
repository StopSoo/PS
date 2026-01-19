// https://school.programmers.co.kr/learn/courses/30/lessons/181894?language=javascript

// 내 답안
function solution(arr) {
    var sIndex = arr.indexOf(2);
    var eIndex = [...arr].reverse().indexOf(2);
    if (eIndex !== -1) eIndex = arr.length - eIndex - 1;

    if (sIndex === -1) return [-1];
    else if (sIndex === eIndex) return [arr[sIndex]];
    else return arr.slice(sIndex, eIndex + 1);
}

// 좀 더 간결한 답안
// indexOf() 함수와 함께 lastIndexOf() 함수 기억하기 !!
function solution(arr) {
    const from = arr.indexOf(2);
    const end = arr.lastIndexOf(2);

    return from === -1 ? [-1] : arr.slice(from, end + 1);
}