# https://www.acmicpc.net/problem/7562

# 내 답안
# 걸린 시간: 2768ms
# 알고리즘: 그래프 탐색(BFS)
# 좀 더 시간을 단축시키기 위한 방법 -> count 값을 덱에 넣지 말고 visited 배열에 저장하기.
import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
  I = int(input())
  ny, nx = map(int, input().split())
  dy, dx = map(int, input().split())

  deq = deque([(ny, nx, 0)])
  visited = [[False] * I for _ in range(I)] # 방문 체크 배열
  visited[ny][nx] = True # 시작점 방문 체크
  while deq:
    y, x, count = deq.popleft()
    if y == dy and x == dx: # 목적지에 도달한다면 종료
      print(count)
      break

    for cy, cx in [(y-1, x-2), (y-2, x-1), (y-2, x+1), (y-1, x+2), (y+1, x-2), (y+2, x-1), (y+2, x+1), (y+1, x+2)]:
      if 0 <= cy < I and 0 <= cx < I and not visited[cy][cx]:
        visited[cy][cx] = True
        deq.append((cy, cx, count + 1))