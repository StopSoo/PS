# https://www.acmicpc.net/problem/6593

# 내 답안
# 걸린 시간: 172ms
# 알고리즘: 그래프 탐색(BFS)
import sys
input = sys.stdin.readline
from collections import deque

while True:
  L, R, C = map(int, input().split())
  if L == 0 and R == 0 and C == 0: break

  miro = []
  for _ in range(L):
    miro.append([list(input().strip()) for _ in range(R)])
    l = input().strip() # 빈 줄 skip
  
  s_pos, e_pos = [], []
  for i in range(L):
    for j in range(R):
      for k in range(C):
        if miro[i][j][k] == 'S': s_pos = [i, j, k]
        if miro[i][j][k] == 'E': e_pos = [i, j, k]

  visited = [[[-1] * C for _ in range(R)] for _ in range(L)]
  deq = deque([s_pos])
  visited[s_pos[0]][s_pos[1]][s_pos[2]] = 0
  while deq:
    h, y, x = deq.popleft()

    for nh, ny, nx in [(h, y-1, x), (h, y, x+1), (h, y+1, x), (h, y, x-1), (h+1, y, x), (h-1, y, x)]:
      if (0 <= nh < L and 0 <= ny < R and 0 <= nx < C) and (visited[nh][ny][nx] == -1):
        if miro[nh][ny][nx] == '.':
          deq.append((nh, ny, nx))
        visited[nh][ny][nx] = visited[h][y][x] + 1 # 벽이든 갈 수 있는 공간이든 방문 체크는 다 하기

        if miro[nh][ny][nx] == 'E':
          print(f"Escaped in {visited[e_pos[0]][e_pos[1]][e_pos[2]]} minute(s).")
          break   
  if visited[e_pos[0]][e_pos[1]][e_pos[2]] == -1: print("Trapped!")
