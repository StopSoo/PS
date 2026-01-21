// https://school.programmers.co.kr/learn/courses/30/lessons/181881?language=javascript

// 내 답안
// 두 배열이 온전히 똑같은지 확인 => JSON.stringify(배열1) === JSON.stringify(배열2)
function solution(arr) {
    var count = 0;
    var new_arr = [];
    while (true) {
        count += 1;
        new_arr = arr.map((e) =>
            e >= 50 && !(e % 2) ? e / 2 : e < 50 && e % 2 ? e * 2 + 1 : e,
        );

        if (JSON.stringify(arr) == JSON.stringify(new_arr)) break;
        else arr = [...new_arr]; // 무조건 spread 연산자로 !!!
    }
    return count - 1;
}