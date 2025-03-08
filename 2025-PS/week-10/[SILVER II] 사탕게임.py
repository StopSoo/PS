# https://www.acmicpc.net/problem/3085

# 내 답안
# 걸린 시간: 2792ms
# 브루트포스로 가능한지 확인할 때 -> 상하좌우 확인 (4N^2) * 열/행 확인 (2N^2) = 8N^4
# 최대 연속 문자열 세기 -> 선형 탐색 (!)
def get_best():
  global N, colors
  best = 0
  # rows
  for i in range(N):
    bef = '-'
    value = 0
    for j in range(N):
      if colors[i][j] == bef: value += 1
      else: value = 1
      bef = colors[i][j]
      best = max(best, value)
  # columns
  for j in range(N):
    bef = '-'
    value = 0
    for i in range(N):
      if colors[i][j] == bef: value += 1
      else: value = 1
      bef = colors[i][j]
      best = max(best, value)
  
  return best

dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]

import sys
input = sys.stdin.readline

N = int(input())
colors = [list(input().strip()) for _ in range(N)]
answer = 0

for y in range(N):
  for x in range(N):
    for i in range(4):
      ny, nx = y + dy[i], x + dx[i]
      if 0 <= ny < N and 0 <= nx < N:
        if colors[ny][nx] != colors[y][x]:
          colors[ny][nx], colors[y][x] = colors[y][x], colors[ny][nx] # 교환
          answer = max(answer, get_best())
          colors[ny][nx], colors[y][x] = colors[y][x], colors[ny][nx] # 복구

print(answer)