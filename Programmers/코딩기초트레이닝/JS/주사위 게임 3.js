// https://school.programmers.co.kr/learn/courses/30/lessons/181916?language=javascript

// 너무 시간이 오래 걸려서 도움 받음 => JS 문법과 함께 복습 필요 !!
function solution(a, b, c, d) {
    const dice = [a, b, c, d];
    const counts = {}; // object

    for (const num of dice) { // 배열 순회할 때 of 
        counts[num] = (counts[num] || 0) + 1; // js는 or 대신 ||
    }

    const keys = Object.keys(counts).map(Number); // 객체의 key들만 뽑아서 배열로 반환, Number화하기
    const valCount = keys.length;
    // 1. 네 주사위 숫자가 모두 같을 때
    if (valCount === 1) {
        return 1111 * keys[0];
    }
    // 2. 세 숫자가 같고 하나가 다를 때 OR 두 개씩 같을 때
    if (valCount === 2) {
        const [p, q] = keys; // 구조 분해 할당
        if (counts[p] === 3 || counts[q] === 3) {
            // 세 숫자가 같은 경우
            const realP = counts[p] === 3 ? p : q;
            const realQ = counts[p] === 3 ? q : p;
            return Math.pow(10 * realP + realQ, 2);
        } else {
            // 두 개씩 같은 경우 (2:2)
            return (p + q) * Math.abs(p - q); // 절댓값은 Math.abs()
        }
    }
    // 3. 두 숫자가 같고 나머지 두 개가 서로 다를 때 (2:1:1)
    if (valCount === 3) {
        // 빈도수가 1인 숫자들만 곱함
        let result = 1;
        for (const key of keys) {
            if (counts[key] === 1) {
                result *= key;
            }
        }
        return result;
    }
    // 4. 네 숫자가 모두 다를 때
    if (valCount === 4) {
        return Math.min(...dice); // Math.min() 함수 내부에 배열 넣을 때 spread
    }
}