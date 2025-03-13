# https://www.acmicpc.net/problem/2667

# 내 답안
# 걸린 시간: 32ms
# 푸는 데 한 30분 걸린 듯 ? DFS로 풀이.
dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]

def find_group(y, x):
  global N, town, dy, dx, visited, depth

  visited[y][x] = True
  depth += 1

  for i in range(4):
    ny, nx = y + dy[i], x + dx[i]
    if (0 <= ny < N and 0 <= nx < N) and (not visited[ny][nx]) and (town[ny][nx] == '1'):
      find_group(ny, nx)

N = int(input())
town = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

count = [] # 단지 별 집 수
for r in range(N):
  for c in range(N):
    if (town[r][c] == '1') and (not visited[r][c]):
      depth = 0
      find_group(r, c)
      count.append(depth)

print(len(count))
print(*sorted(count), sep='\n')