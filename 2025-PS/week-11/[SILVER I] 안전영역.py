# https://www.acmicpc.net/problem/2468

# 내 답안
# 걸린 시간: 1136ms
# "아무 지역도 안 잡길 수 있다" -> 비교할 height가 0부터 시작한다는 뜻 !!
# 난 DFS를 사용했지만, deque를 활용해 BFS로도 구현 가능!
import sys
sys.setrecursionlimit(1000000)

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

def find_area(y, x, height):
  global dy, dx, visited, ground

  visited[y][x] = True

  for i in range(4):
    ny, nx = y + dy[i], x + dx[i]
    if (0 <= ny < N and 0 <= nx < N) and (not visited[ny][nx]):
      if ground[ny][nx] > height:
        find_area(ny, nx, height)
      else:
        visited[ny][nx] = True
  return 1

N = int(input())
ground = [list(map(int, input().split())) for _ in range(N)]

max_count = 0 # 제출할 정답
for height in range(0, 101):
  count = 0 # 이번 height에서 안전영역의 개수
  visited = [[False] * N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      if (ground[i][j] > height) and (not visited[i][j]): 
        count += find_area(i, j, height)
  max_count = max(max_count, count)

print(max_count)