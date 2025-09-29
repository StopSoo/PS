# https://www.acmicpc.net/problem/3184

# 내 답안
# 걸린 시간: 172ms
# 알고리즘: 그래프 탐색
from collections import deque

R, C = map(int, input().split())
ground = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

sheep, wolf = 0, 0 # 양, 늑대
for i in range(R):
  for j in range(C):
    s, w = 0, 0 # 구역의 양, 늑대 수
    if not visited[i][j]:
      visited[i][j] = True # 방문 체크
      if ground[i][j] == 'v': w += 1
      elif ground[i][j] == 'o': s += 1

      deq = deque([(i, j)])
      while deq:
        y, x = deq.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          ny, nx = y + dy, x + dx
          if 0 <= ny < R and 0 <= nx < C and not visited[ny][nx]:
            visited[ny][nx] = True
            if ground[ny][nx] == '.':
              deq.append((ny, nx))
            elif ground[ny][nx] == 'o':
              s += 1
              deq.append((ny, nx))
            elif ground[ny][nx] == 'v':
              w += 1
              deq.append((ny, nx))

    if s > w:
      sheep += s
    else:
      wolf += w

print(sheep, wolf)
