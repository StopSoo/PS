# https://www.acmicpc.net/problem/1926

# 내 답안
# 걸린 시간: 632ms
# BFS -> 모든 칸을 순회하면서 1일 때만 주변 영역을 탐색
# 구역 넓이 체크 시 굳이 큐에 넣지 않고 지역 변수로 사용하는 것이 더 효율적 (!)
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().strip().split())
paint = list(list(map(int, input().strip().split())) for _ in range(n))
total, max_area = 0, 0
checked = [[0] * m for _ in range(n)] # 방문 체크 배열

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(n):
  for j in range(m):
    if paint[i][j] == 1 and not checked[i][j]: 
      total += 1 # 그림 개수 증가
      area = 1 # 구역 넓이 체크
      deq = deque()
      deq.append((i, j))
      checked[i][j] = 1

      while deq:
        y, x = deq.popleft()
        for k in range(4):
          ny, nx = y + dy[k], x + dx[k]
          if 0 <= ny < n and 0 <= nx < m:
            if paint[ny][nx] == 1 and not checked[ny][nx]:
              deq.append((ny, nx))
              checked[ny][nx] = 1
              area += 1
      max_area = max(max_area, area) # 넓이의 최댓값 체크

print(total)
print(max_area if total else 0)