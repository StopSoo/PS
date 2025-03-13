# https://www.acmicpc.net/problem/21736

# 내 답안
# 걸린 시간: 344ms
# DFS를 사용했으나 시간초과가 나서, 스택을 사용한 DFS로 변경 (!)
import sys
input = sys.stdin.readline

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

def find_friends(y, x):
  global N, M, dy, dx, ground, visited, count
  
  stack = [(y, x)] # 스택 사용 -> 스택 오버플로우 해결
  visited[y][x] = True

  while stack:
    y, x = stack.pop()

    for i in range(4):
      ny, nx = y + dy[i], x + dx[i]
      
      if (0 <= ny < N and 0 <= nx < M) and (not visited[ny][nx]):
        visited[ny][nx] = True # 여기서 방문 체크 (!)
        if ground[ny][nx]=='O':
          stack.append((ny, nx))
        elif ground[ny][nx]=='P':
          count += 1
          stack.append((ny, nx))

N, M = map(int, input().split())
ground = [list(input().strip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

now = None # 도연이의 현재 위치
for i in range(N):
  for j in range(M):
    if ground[i][j] == 'I': 
      now = (i, j)
      break
  if now: break

count = 0
find_friends(now[0], now[1])
print(count if count else 'TT')