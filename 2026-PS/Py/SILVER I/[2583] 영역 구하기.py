# https://www.acmicpc.net/problem/2583
# 260226 풀이
# 알고리즘: 그래프 탐색(BFS)
# 시간: 72ms

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

import sys
from collections import deque
input = sys.stdin.readline

M, N, K = map(int, input().strip().split())
area = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().strip().split())
    for row in range(y1, y2):
        for col in range(x1, x2):
            area[row][col] = 1

count = 0 # 영역의 개수
values = [] # 영역의 넓이
for i in range(M):
    for j in range(N):
        if not area[i][j]: # 값이 0이면 (방문X or 직사각형 내부가 아님)
            area[i][j] = 1
            count += 1

            deq = deque([(i, j)])
            value = 0
            while deq:
                y, x = deq.popleft()
                value += 1
                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if 0 <= ny < M and 0 <= nx < N and not area[ny][nx]:
                        deq.append((ny, nx))
                        area[ny][nx] = 1
            values.append(value)

values.sort()
print(count) # values 배열 길이로 대체 가능할 듯
print(*values)