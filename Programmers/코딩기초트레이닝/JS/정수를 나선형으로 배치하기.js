// https://school.programmers.co.kr/learn/courses/30/lessons/181832?language=javascript

// 해결 못 함
function solution(n) {
    const answer = Array.from({ length: n }, () => Array(n).fill(0)); // n X n 배열

    const dr = [0, 1, 0, -1];
    const dc = [1, 0, -1, 0];

    let r = 0, c = 0, dir = 0;

    for (let i = 1; i <= n * n; i++) {
        answer[r][c] = i;

        let nr = r + dr[dir];
        let nc = c + dc[dir];
        // 3. 방향 전환 조건 체크
        // 범위를 벗어나거나, 이미 숫자가 채워져 있다면 방향 전환
        if (nr < 0 || nr >= n || nc < 0 || nc >= n || answer[nr][nc] !== 0) {
            dir = (dir + 1) % 4; // 방향을 다음 순서로 바꿈
            nr = r + dr[dir];
            nc = c + dc[dir];
        }
        // 위치 이동
        r = nr;
        c = nc;
    }

    return answer;
}