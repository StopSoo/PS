# https://www.acmicpc.net/problem/1012

# 내 답안
# 걸린 시간: 44ms
# recursionError 뜨면 setrecursionlimit 추가하기 !! 
# DFS 사용 -> 재귀 사용 시 주의 !!
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000) 

dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]

def count_animal(y, x):
  global m, n, dy, dx, ground, visited
  
  visited[y][x] = True # 방문 체크
  
  for i in range(4):
    ny, nx = y + dy[i], x + dx[i]
    if (0 <= ny < n and 0 <= nx < m) and (not visited[ny][nx]) and (ground[ny][nx] == 1):
      count_animal(ny, nx)
  return 1

T = int(input())
for _ in range(T):
  m, n, k = map(int, input().strip().split())
  ground = [[0] * m for _ in range(n)]
  visited = [[False] * m for _ in range(n)] # 방문 배열
  count = 0 # 제출할 정답
  
  for _ in range(k): # 배추가 있는 곳 입력 받고 체크
    x, y = map(int, input().strip().split())
    ground[y][x] = 1

  for i in range(n):
    for j in range(m):
      if (ground[i][j] == 1) and (not visited[i][j]):
        count += count_animal(i, j) # 이어진 모든 곳 방문 체크

  print(count)