# https://www.acmicpc.net/problem/7569
# 260404 풀이
# 알고리즘: 그래프 / 최단 경로
# 시간: 3684ms

# 느낀 점
# 1) 3차원 배열이니까 dz 사용하기
# 2) 인덱싱할 때도 z부터 하기 !!
import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

M, N, H = map(int, input().strip().split())
tomatoes = [[list(map(int, input().strip().split())) for _ in range(N)] for _ in range(H)]

day = 0
deq = deque([(i, j, k, day) for i in range(N) for j in range(M) for k in range(H) if tomatoes[k][i][j] == 1])
while deq:
    y, x, z, d = deq.popleft()
    for i in range(6):
        ny, nx, nz = y + dy[i], x + dx[i], z + dz[i]
        if 0 <= ny < N and 0 <= nx < M and 0 <= nz < H and tomatoes[nz][ny][nx] == 0:
            tomatoes[nz][ny][nx] = d + 1
            deq.append((ny, nx, nz, d + 1))
            day = d + 1

if any(0 in row for ground in tomatoes for row in ground): print(-1)
else: print(day)