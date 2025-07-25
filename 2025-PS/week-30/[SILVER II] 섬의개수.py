# https://www.acmicpc.net/problem/4963

# 내 답안
# 걸린 시간: 88ms
import sys
input = sys.stdin.readline
from collections import deque

while True:
  w, h = map(int, input().split())
  if w == h == 0: 
    break
  
  miro = [list(map(int, input().split())) for _ in range(h)]
  checked = [[0] * w for _ in range(h)] # 방문 체크 배열

  count = 0 # 섬의 개수
  for i in range(h):
    for j in range(w):
      if not checked[i][j]:
        if miro[i][j] == 0:
          checked[i][j] = 1
        else:
          count += 1
          deq = deque([(i, j)])
          checked[i][j] = 1
          while deq:
            y, x = deq.popleft()
            for dy, dx in [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
              ny, nx = y + dy, x + dx
              if 0 <= ny < h and 0 <= nx < w and not checked[ny][nx] and miro[ny][nx] == 1:
                checked[ny][nx] = 1
                deq.append((ny, nx))
  print(count)