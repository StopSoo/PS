# https://www.acmicpc.net/problem/1743

# 내 답안
# 걸린 시간: 68ms
# BFS/DFS에서는 큐(스택)에 넣는 순간 방문 처리가 안전하다(!)
import sys
input = sys.stdin.readline
from collections import deque

N, M, K = map(int, input().strip().split())
miro = [['.'] * (M + 1) for _ in range(N + 1)]
for _ in range(K):
  r, c = map(int, input().strip().split())
  miro[r][c] = '#'

max_size = 0
for i in range(1, N + 1):
  for j in range(1, M + 1):
    if miro[i][j] == '#':
      deq = deque([(i, j)])
      miro[i][j] = '.' # 시작점 방문 체크
      size = 0
      while deq:
        y, x = deq.popleft()
        size += 1
        for dy, dx in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
          ny, nx = y + dy, x + dx
          if 1 <= ny <= N and 1 <= nx <= M and miro[ny][nx] == '#':
            miro[ny][nx] = '.' # 방문 처리를 미리 할 것(!)
            deq.append((ny, nx))
      max_size = max(max_size, size)

print(max_size)