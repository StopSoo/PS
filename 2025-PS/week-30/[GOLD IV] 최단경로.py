# https://www.acmicpc.net/problem/1753

# 내 답안
# 걸린 시간: 740ms
# 알고리즘: 다익스트라
# 노드 별 방문 체크를 할 필요는 없음을 (!)
import sys, heapq
input = sys.stdin.readline
INF = float('inf')

V, E = map(int, input().split())
start = int(input())
graph = {v: [] for v in range(1, V + 1)}
for _ in range(E):
  u, v, w = map(int, input().split())
  graph[u].append((v, w)) # (종점, 거리)

weights = [INF] * (V + 1)
q = []
heapq.heappush(q, (0, start)) # (거리, 노드)
weights[start] = 0 # 거리 초기화
while q:
  dist, node = heapq.heappop(q)
  if weights[node] < dist: continue
  for neighbor, w in graph[node]:
    if weights[neighbor] > dist + w: # 갱신할 필요가 있을 때만 체크
      weights[neighbor] = dist + w # 갱신
      heapq.heappush(q, (dist + w, neighbor))

# 출력
for i in range(1, V + 1):
  print(weights[i] if weights[i] != INF else "INF")