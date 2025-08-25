# https://www.acmicpc.net/problem/31575

# 내 답안
# 걸린 시간: 140ms
# 알고리즘: DFS
# 문제를 잘 읽자 !
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(y, x):
  global city, checked, N, M

  if y == M-1 and x == N-1: # 도착지에 도착하면 탐색 X
    return
  
  for dy, dx in [[1, 0], [0, 1]]: # 동쪽, 남쪽으로만 이동 가능
    ny, nx = y + dy, x + dx
    if 0 <= ny < M and 0 <= nx < N and city[ny][nx] and not checked[ny][nx]:
      checked[ny][nx] = 1
      dfs(ny, nx)

N, M = map(int, input().strip().split())
city = [list(map(int, input().strip().split())) for _ in range(M)]

checked = [[0] * N for _ in range(M)]
checked[0][0] = 1
dfs(0, 0)
print("Yes" if checked[M-1][N-1] else "No")