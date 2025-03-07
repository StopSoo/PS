# https://www.acmicpc.net/problem/14940

# 내 답안
# 걸린 시간: 792ms
# BFS로 풀이.
import sys
input = sys.stdin.readline
from collections import deque
# 상하좌우 이동 좌표
dy = [-1, 0, 1, 0] 
dx = [0, 1, 0, -1]

n, m = map(int, input().strip().split())
miro = [[0 for _ in range(m+1)]] + [[0] + list(map(int, input().strip().split())) for _ in range(n)]
answer = miro[:] # 정답

target = []
for i in range(1, n+1):
  for j in range(1, m+1):
    if miro[i][j] == 2: target = [i, j] # 목표 위치 저장 

deq = deque()
visited = [[False for _ in range(m+1)] for _ in range(n+1)] # 방문 배열

deq.append((target[0], target[1], 0)) # (x좌표, y좌표, 누적 거리)
visited[target[0]][target[1]] = True # 방문 체크

while deq:
  y, x, dist = deq.popleft()
  answer[y][x] = dist

  for i in range(4):
    ny, nx = y + dy[i], x + dx[i]
    if (1 <= ny <= n and 1 <= nx <= m) and (not visited[ny][nx]) and (miro[ny][nx] == 1):
      deq.append((ny, nx, dist+1))
      visited[ny][nx] = True

for i in range(1, n+1):
  for j in range(1, m+1):
    if not visited[i][j] and miro[i][j] == 1: answer[i][j] = -1
# 최종 출력 
for i in range(1, n+1):
  for j in range(1, m+1):
    print(answer[i][j], end=' ')
  print()