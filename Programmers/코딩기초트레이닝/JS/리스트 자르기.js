// https://school.programmers.co.kr/learn/courses/30/lessons/181897?language=javascript

// 내 답안
// 자바스크립트에서는 간격을 지정해서 슬라이싱할 수 없다.
function solution(n, slicer, num_list) {
    let [a, b, c] = slicer; // 구조 분해 할당(!)
    
    if (n === 1)
        return num_list.slice(0, b + 1);
    else if (n === 2) 
        return num_list.slice(a);
    else if (n === 3)
        return num_list.slice(a, b + 1);
    else
        return num_list.filter((_, i) => i >= a && i <= b && (a + i) % c === 0);
    // n === 4의 경우는 return문을 아래와 같이 작성할 수도 있다.
    // return num_list.slice(a, b + 1).filter((_, idx) => !(idx % c));
}