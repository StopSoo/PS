# https://www.acmicpc.net/problem/2638

# 내 답안
# 걸린 시간: 1168ms
# 1. 처음에는 치즈 내부 영역과 치즈 외부 공기를 어떻게 분리할지 고민함.
# 2. 치즈가 녹은 후 외부 공기를 체크하는 것도 BFS로 처리했어야 하는데 그냥 브루트포스로 한 게 문제.
# 3. -1로 바꾸는 시점 같은 부분에서 많이 헷갈림.
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
paper = list(list(map(int, input().split())) for _ in range(N))
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
# 전체 영역에 치즈가 남아있는지 확인하는 함수
def has_cheese():
  for i in range(N):
    for j in range(M):
      if paper[i][j] == 1: return True
  return False
# 외부 공기 구별하는 함수
def mark_outside_air():
  visited = [[False] * M for _ in range(N)]
  deq = deque([(0, 0)])
  visited[0][0] = True
  paper[0][0] = -1

  while deq:
    y, x = deq.popleft()
    for i in range(4):
      ny, nx = y + dy[i], x + dx[i]
      if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
        visited[ny][nx] = True # 방문 체크

        if paper[ny][nx] == 0:
          paper[ny][nx] = -1 # 외부 공기로 체크
          deq.append((ny, nx))
        elif paper[ny][nx] == -1: # 탐색만 진행
          deq.append((ny, nx))
# 초기 외부 공기 표시
mark_outside_air() 

time = 0 # 걸리는 시간
while has_cheese():
  changed_pos = []
  for y in range(N):
    for x in range(M):
      if paper[y][x] == 1:
        count = 0 # 외부 공기와 닿는 면 수
        for i in range(4):
          ny, nx = y + dy[i], x + dx[i]
          if 0 <= ny < N and 0 <= nx < M and paper[ny][nx] == -1: count += 1
        if count >= 2: 
          changed_pos.append((y, x))

  for cy, cx in changed_pos:
    paper[cy][cx] = 0 # 일단 치즈가 녹으면 없앰
  
  mark_outside_air() # 녹은 치즈를 고려해서 외부 공기 다시 체크 
  time += 1 # 시간 증가

print(time)