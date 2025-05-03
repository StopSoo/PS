# https://www.acmicpc.net/problem/2206

# 내 답안
# 걸린 시간: 3716ms
# 알고리즘: BFS
# 처음 풀 때 막힌 부분: 벽을 부수고 방문했을 때와 부수지 않고 방문했을 때를 모두 하나의 배열로 처리해서 예외 케이스가 생김.
# 해결 방법: [벽을 부수지 않고 방문, 벽을 부수고 방문] 으로 변경해서 checked 배열을 3차원 배열로 만듬 (!)
import sys
input = sys.stdin.readline
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
  global miro, checked, dy, dx

  q = deque()
  q.append((y, x, False, 1)) # y좌표, x좌표, 부숨 여부, 최단 경로
  checked[y][x][0] = True # 벽을 부수지 않고 방문한 것 체크

  while q:
    ny, nx, is_brake, count = q.popleft()
    if ny == N-1 and nx == M-1: return count # 목적지에 도달하면 count 반환
    for i in range(4):
      new_y, new_x = ny + dy[i], nx + dx[i]
      if 0 <= new_y < N and 0 <= new_x < M:
        # 현재 0인데, 부수지 않고 방문한 적이 없다면
        if miro[new_y][new_x] == '0' and not checked[new_y][new_x][is_brake]:
          checked[new_y][new_x][is_brake] = True # 방문 체크
          q.append((new_y, new_x, is_brake, count+1))
        # 현재 1인데, 지금까지 한 번도 부수지 않았고, 부수고 방문한 적이 없다면
        elif miro[new_y][new_x] == '1' and is_brake == False and not checked[new_y][new_x][1]:
          checked[new_y][new_x][1] = True
          q.append((new_y, new_x, True, count+1))

  return -1 # 목적지에 도달하지 못하면 -1 반환

N, M = map(int, input().strip().split())
miro = list(list(input().strip()) for _ in range(N))
checked = [[[False] * 2 for _ in range(M)] for _ in range(N)] # [벽을 부수지 않고 방문, 벽을 부수고 방문]
print(bfs(0, 0))