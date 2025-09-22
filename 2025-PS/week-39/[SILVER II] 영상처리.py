# https://www.acmicpc.net/problem/21938

# 내 답안
# 걸린 시간: 1172ms
# 알고리즘: 그래프 이론
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().strip().split())
screen = [[0] * M for _ in range(N)] # 영상 처리된 배열
values = [list(map(int, input().strip().split())) for _ in range(N)]
T = int(input().strip())
for i in range(N):
  for j in range(M):
    s = sum(values[i][j*3:(j+1)*3]) // 3
    if s >= T:
      screen[i][j] = 255
    else:
      screen[i][j] = 0
# 그래프 탐색
visited = [[False] * M for _ in range(N)]
count = 0
for i in range(N):
  for j in range(M):
    if not visited[i][j] and screen[i][j] == 255:
      deq = deque([(i, j)])
      while deq:
        y, x = deq.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          ny, nx = y + dy, x + dx
          if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] \
            and screen[ny][nx] == 255:
            visited[ny][nx] = True
            deq.append((ny, nx))
      count += 1

print(count)