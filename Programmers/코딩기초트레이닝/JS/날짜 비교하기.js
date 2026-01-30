// https://school.programmers.co.kr/learn/courses/30/lessons/181838?language=javascript

// 내 답안
function solution(date1, date2) {
    var answer = 0;
    for (let i = 0; i < 3; i++) {
        if (date1[i] < date2[i]) {
            answer = 1;
            break;
        } else if (date1[i] > date2[i]) break;
        // 같을 때는 continue
    }
    return answer;
}
// 좀 더 간결하고 좋은 답안
const solution = (date1, date2) => (new Date(date1) < new Date(date2) ? 1 : 0);