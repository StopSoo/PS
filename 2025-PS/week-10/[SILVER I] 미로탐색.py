# https://www.acmicpc.net/problem/2178

# 내 답안
# 걸린 시간: 76ms
# 가중 그래프가 아닌 경우에서의 최단 경로는 BFS를 활용할 수 있다 (!)
# 그래프 문제라고 생각을 못 했는데, 그래프로 생각할 수 있는 사고력을 길러야겠다. 
from collections import deque
# 상하좌우 이동 좌표
dy = [-1, 0, 1, 0] 
dx = [0, 1, 0, -1]

N, M = map(int, input().split())
miro = ['0' * (M+1)] + ['0' + input() for _ in range(N)] # 미로가 붙어서 출력되므로 0을 포함해서 왼쪽과 같이 설정

deq = deque()
visited = [[False] * (M+1) for _ in range(N+1)] # 2차원 방문 배열

deq.append((1, 1, 1)) # 시작 위치(1, 1), 지난 칸의 개수
visited[1][1] = True

while deq:
  y, x, dist = deq.popleft()

  if y == N and x == M:
    print(dist)
    break
  
  for i in range(4): # 좌표를 이동해가면서 비교
    ny, nx = y + dy[i], x + dx[i]
    if (1 <= ny <= N and 1 <= nx <= M) and (not visited[ny][nx]) and (miro[ny][nx] == '1'):
      deq.append((ny, nx, dist+1))
      visited[ny][nx] = True