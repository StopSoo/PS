# https://www.acmicpc.net/problem/16234

# 내 답안(틀린 코드)
# 알고리즘: 그래프 이론 / BFS
# 내가 짠 코드의 문제점: 전역 집합으로 계산해서 인구 갱신을 하는 게 아니라, 연합 단위로 인구 갱신을 해야 함 (!)
from collections import deque

N, L, R = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(N)]

count = 0 # 인구 이동이 일어나는 횟수
while True:
  visited = [[0] * N for _ in range(N)]
  opened_nations = set() # 국경선이 열린 국가들의 좌표
  s, c = 0, 0 # 인구 수의 합과 국가 개수

  for i in range(N):
    for j in range(N):
      visited[i][j] = 1
      is_open = False
      for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny, nx = i + dy, j + dx
        if 0 <= ny < N and 0 <= nx < N and \
          L <= abs(nations[i][j] - nations[ny][nx]) <= R:
          visited[ny][nx] = 1
          opened_nations.add((ny, nx))
          is_open = True
      if is_open: 
        opened_nations.add((i, j))
  
  if not opened_nations: # 인구 이동할 국가가 없으면
    break
  else:
    for y, x in opened_nations:
      s += nations[y][x]
      c += 1
    for y, x in opened_nations:  
      nations[y][x] = (s // c)
    count += 1

print(count)

# 수정된 코드
# 걸린 시간: 5028ms
from collections import deque

N, L, R = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(N)]

def bfs(y, x, visited):
  q = deque([(y, x)])
  union = [(y, x)] # 단위 집합
  visited[y][x] = 1
  total = nations[y][x]

  while q:
    cy, cx = q.popleft()
    for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
      ny, nx = cy + dy, cx + dx
      if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
        if L <= abs(nations[cy][cx] - nations[ny][nx]) <= R:
          visited[ny][nx] = 1
          q.append((ny, nx))
          union.append((ny, nx))
          total += nations[ny][nx]
  return union, total

count = 0
while True:
    visited = [[0] * N for _ in range(N)]
    moved = False

    for i in range(N):
      for j in range(N):
        if not visited[i][j]:
          union, total = bfs(i, j, visited)
          if len(union) > 1: # 연합이 만들어졌다면
            moved = True
            new_pop = total // len(union)
            for y, x in union:
              nations[y][x] = new_pop
    if not moved:
      break
    count += 1

print(count)
