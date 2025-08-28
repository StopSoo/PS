# https://www.acmicpc.net/problem/2458

# 내 답안
# 걸린 시간: 1376ms(pypy3)
# 알고리즘: 플로이드-워셜 -> N이 최대 500이라 python에서는 시간초과
# 개선 방향: 필요 없는 연산 제거 & pypy 사용
import sys
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().strip().split())
matrix = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1): matrix[i][i] = 0 # 대각선은 0으로 체크
for _ in range(M):
  a, b = map(int, input().strip().split())
  matrix[a][b] = 1 # 갈 수 있으면 1

for k in range(1, N + 1): # 거쳐가는 노드
  for i in range(1, N + 1): # 시작점
    for j in range(1, N + 1): # 끝점
      if i != j and matrix[i][k] != INF and matrix[k][j] != INF: # 필요없는 연산 제거
        if matrix[i][j] > matrix[i][k] + matrix[k][j]:
          matrix[i][j] = matrix[i][k] + matrix[k][j]
# 정답 체크
count = 0
for node in range(1, N + 1): # 체크하는 노드
  for other in range(1, N + 1):
    if matrix[node][other] == INF and matrix[other][node] == INF:
      break
  else: count += 1 # 키가 몇 번째인지 알 수 있는 노드!
print(count)

# BFS를 활용한 개선된 코드
# 아이디어: 역그래프를 활용해서 내가 갈 수 있는 노드 + 나에게 올 수 있는 노드 = N-1 조건 체크하기
# 걸린 시간: 252ms(pypy3) / 1220ms(python3)
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
reverse_graph = [[] for _ in range(N+1)]

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  reverse_graph[b].append(a)

def bfs(start, g):
  visited = [False] * (N+1)
  q = deque([start])
  visited[start] = True
  cnt = 0
  while q:
    cur = q.popleft()
    for nxt in g[cur]:
      if not visited[nxt]:
        visited[nxt] = True
        q.append(nxt)
        cnt += 1
  return cnt

count = 0
for node in range(1, N+1):
  smaller = bfs(node, graph)       # 자신보다 작은 노드 개수
  bigger = bfs(node, reverse_graph) # 자신보다 큰 노드 개수
  if smaller + bigger == N - 1:    # 모든 노드와 비교 가능
    count += 1

print(count)