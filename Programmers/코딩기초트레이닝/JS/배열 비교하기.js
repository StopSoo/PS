// https://school.programmers.co.kr/learn/courses/30/lessons/181856

function solution(arr1, arr2) {
    if (arr1.length !== arr2.length)
        return arr1.length > arr2.length ? 1 : -1;
    else {
        var sum1 = arr1.reduce((acc, ele) => acc + ele, 0);
        var sum2 = arr2.reduce((acc, ele) => acc + ele, 0);
        return sum1 > sum2 ? 1 : sum1 === sum2 ? 0 : -1;
    }
}