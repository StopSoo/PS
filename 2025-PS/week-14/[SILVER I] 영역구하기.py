# https://www.acmicpc.net/problem/2583

# 내 답안
# 걸린 시간: 48ms
import sys
sys.setrecursionlimit(1000000)

def dfs(y, x):
  global M, N, check, area, count

  dy = [-1, 1, 0, 0]
  dx = [0, 0, -1, 1]

  check[y][x] = 1
  count += 1
  for i in range(4):
    ny, nx = y + dy[i], x + dx[i]
    if 0 <= ny < M and 0 <= nx < N and not check[ny][nx]:
      dfs(ny, nx)

M, N, K = map(int, input().split())
check = [[0]*N for _ in range(M)]
for _ in range(K):
  x1, y1, x2, y2 = map(int, input().split())
  for y in range(y1, y2):
    for x in range(x1, x2):
      check[y][x] = 1

areas = []
for y in range(M):
  for x in range(N):
    if check[y][x] == 0: 
      count = 0
      dfs(y, x)
      areas.append(count)

print(len(areas))
print(*sorted(areas))