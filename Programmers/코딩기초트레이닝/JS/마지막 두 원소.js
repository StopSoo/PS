// https://school.programmers.co.kr/learn/courses/30/lessons/181927?language=javascript

// 내 답안
function solution(num_list) {
    var answer = [...num_list];
    let l = answer.length;
    if (answer[l - 1] > answer[l - 2]) answer.push(answer[l - 1] - answer[l - 2]);
    else answer.push(answer[l - 1] * 2);

    return answer;
}

// 깔끔하고 간결한 코드 
function solution(num_list) {
    const [a, b] = [...num_list].reverse();
    return [...num_list, a > b ? a - b : a * 2];
}