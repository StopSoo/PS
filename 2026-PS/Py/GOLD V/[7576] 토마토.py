# https://www.acmicpc.net/problem/7576
# 260404 풀이
# 알고리즘: 그래프 / 최단 경로
# 시간: 2268ms

# 느낀 점
# 1) 오늘 새로 익은 토마토만 다음 날에 체크하면 된다(!) -> 배열 전체를 매번 훑는 것은 비효율적이다.
# 2) all() / any() 함수 사용법
# 3) deque를 사용하는 것
import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

M, N = map(int, input().strip().split())
tomatoes = [list(map(int, input().strip().split())) for _ in range(N)]

day = 0
deq = deque([(i, j, day) for j in range(M) for i in range(N) if tomatoes[i][j] == 1])
while deq:
    y, x, d = deq.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and tomatoes[ny][nx] == 0:
            tomatoes[ny][nx] = d + 1
            deq.append((ny, nx, d + 1))
            day = d + 1

if any(0 in row for row in tomatoes): print(-1)
else: print(day)