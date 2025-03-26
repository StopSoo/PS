# https://www.acmicpc.net/problem/14500

# 답안
# 걸린 시간: 4056ms(python3) / 736ms(pypy3)
# 푸는 방법 1) 노가다
# 푸는 방법 2) DFS -> 'ㅗ' / 'ㅗ'를 제외한 나머지 모양들
# 일반 사방향 탐색과 다르게 모든 경우를 다 따져야 한다고 생각했는데, 깊이가 4인 DFS였음을 (!)
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)] # 방문 체크 배열

dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]
maximum = 0 # 최댓값 저장 변수
# ㅗ 모양을 제외한 나머지 모양 탐색
def dfs(y, x, now, count):
  global maximum, dy, dx

  if count == 4: # 탐색 완료 후 최댓값 비교
    maximum = max(maximum, now)
    return 
  for i in range(4):
    ny, nx = y + dy[i], x + dx[i]
    if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
      visited[ny][nx] = True # 방문 체크
      dfs(ny, nx, now+graph[ny][nx], count+1)
      visited[ny][nx] = False # 방문 체크 해제
# ㅗ 모양 탐색
def fy(y, x):
  global maximum, dy, dx

  temp = graph[y][x]
  arr = []
  for i in range(4):
    ny, nx = y + dy[i], x + dx[i]
    if 0 <= nx < M and 0 <= ny < N:
      arr.append(graph[ny][nx])
  if len(arr) == 4: # 네 방향 모두 가능하다면 그 중 가장 작은 값 제거 후 sum
    arr.sort(reverse=True)
    arr.pop()
    maximum = max(maximum, sum(arr) + graph[y][x])
  elif len(arr) == 3: # 세 방향만 가능하기 때문에 바로 sum
    maximum = max(maximum, sum(arr) + graph[y][x])
  return # len(arr)이 2 이하라면 ㅗ 모양이 아니므로 pass

for i in range(N):
  for j in range(M):
    visited[i][j] = True # 현재 지점 방문 체크
    dfs(i, j, graph[i][j], 1)
    fy(i, j)
    visited[i][j] = False # 현재 지점 방문 체크 해제 

print(maximum)