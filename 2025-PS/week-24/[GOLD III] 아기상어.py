# https://www.acmicpc.net/problem/16236

# 답안
# 걸린 시간: 92ms
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
miro = list(list(map(int, input().split())) for _ in range(N))   

# 초기 상어 위치 찾기
for i in range(N):
  for j in range(N):
    if miro[i][j] == 9:
      shark_y, shark_x = i, j
      miro[i][j] = 0

size_shark = 2 # 아기 상어의 크기
eat_count = 0 # 먹은 물고기 개수
time_total = 0

def bfs(sy, sx, size):
  visited = [[False] * N for _ in range(N)]
  q = deque()
  q.append((sy, sx, 0))
  visited[sy][sx] = True
  fishes = []

  while q:
    y, x, dist = q.popleft()
    for dy, dx in [(-1,0), (0,-1), (0,1), (1,0)]:  # 위-왼-오-아 순
      ny, nx = y+dy, x+dx
      if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
        if miro[ny][nx] <= size:
          visited[ny][nx] = True
          if 0 < miro[ny][nx] < size:
            fishes.append((dist+1, ny, nx))
          else:
            q.append((ny, nx, dist+1))
  
  if not fishes:
    return None
  fishes.sort()  # 거리 → y → x 순 정렬
  return fishes[0]  # 가장 가까운 물고기

while True:
  result = bfs(shark_y, shark_x, size_shark)
  if result is None:
    break

  dist, ny, nx = result
  time_total += dist
  eat_count += 1
  miro[ny][nx] = 0
  shark_y, shark_x = ny, nx
  if eat_count == size_shark:
    size_shark += 1
    eat_count = 0

print(time_total)