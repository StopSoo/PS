// https://school.programmers.co.kr/learn/courses/30/lessons/181890?language=javascript

// 처음 짠 코드 (잘못된 코드)
// indexOf() 값이 -1인 경우를 기준으로 분기했는데 그럼 분기 처리가 매우 복잡해짐
function solution(str_list) {
    let [l_idx, r_idx] = [str_list.indexOf("l"), str_list.indexOf("r")];

    if (l_idx === -1 && r_idx === -1)
        return [];
    else if (l_idx < r_idx)
        return str_list.slice(0, l_idx);
    else
        return str_list.slice(r_idx + 1);
}
// 옳은 코드
function solution(str_list) {
    // 배열을 순회하다가 먼저 만난 문자대로 슬라이싱해서 반환
    for (let i = 0; i < str_list.length; i++) {
        if (str_list[i] === "l") {
            return str_list.slice(0, i);
        } else if (str_list[i] === "r") {
            return str_list.slice(i + 1);
        }
    }
    // 배열을 순회하면서 l이나 r을 만나지 못할 경우 빈 배열 반환
    return [];
}