# https://www.acmicpc.net/problem/5972

# 내 답안
# 걸린 시간: 248ms
# 알고리즘: 다익스트라
import sys, heapq
input = sys.stdin.readline
from collections import defaultdict
INF = float('inf')

N, M = map(int, input().strip().split())
graph = defaultdict(list)
for _ in range(M):
  a, b, c = map(int, input().strip().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

def dijkstra():
  q = [(0, 1)] # (거리, 현재 노드)
  d = [INF] * (N + 1)
  d[1] = 0

  while q:
    dist, now = heapq.heappop(q)
    if d[now] < dist: continue # 갱신할 필요 X
    for neighbor, weight in graph[now]:
      if dist + weight < d[neighbor]:
        d[neighbor] = dist + weight
        heapq.heappush(q, (dist + weight, neighbor))
  
  return d

distance = dijkstra()
print(distance[N])