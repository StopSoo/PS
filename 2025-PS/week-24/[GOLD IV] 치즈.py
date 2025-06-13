# https://www.acmicpc.net/problem/2636

# 내 답안
# 걸린 시간: 96ms
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split()) # 세로, 가로
pan = list(list(map(int, input().split())) for _ in range(n))
# 전체 영역에 치즈가 남아있는지 확인하는 함수
def has_cheese():
  count = 0
  for i in range(n):
    for j in range(m):
      if pan[i][j] == 1: count += 1
  return count if count else False
# 외부 공기와 치즈 내부 구멍 구별하는 함수
def mark_outside_air():
  visited = [[False] * m for _ in range(n)]
  deq = deque([(0, 0)])
  visited[0][0] = True       
  pan[0][0] = -1

  while deq:
    y, x = deq.popleft()
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      ny, nx = y + dy, x + dx
      if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
        visited[ny][nx] = True       

        if pan[ny][nx] == 0: 
          pan[ny][nx] = -1 # 외부 공기 체크
          deq.append((ny, nx))
        elif pan[ny][nx] == -1: 
          deq.append((ny, nx))

mark_outside_air(); # 초기 외부 공기 체크

time = 0 # 걸리는 시간
remain_cheese = has_cheese() # 남은 치즈 개수
while remain_cheese:
  changed_pos = []
  for y in range(n):
    for x in range(m):
      if pan[y][x] == 1:
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          ny, nx = y + dy, x + dx          
          if 0 <= ny < n and 0 <= nx < m and pan[ny][nx] == -1: 
            changed_pos.append((y, x))
            break
  for cy, cx in changed_pos: pan[cy][cx] = 0
  mark_outside_air() # 외부 공기 다시 체크
  time += 1
  if has_cheese(): remain_cheese = has_cheese()
  else: break

print(time)
print(remain_cheese)