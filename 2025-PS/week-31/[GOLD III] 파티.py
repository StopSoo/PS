# https://www.acmicpc.net/problem/1238

# 내 답안
# 걸린 시간: 48ms (더 발전함!)
# 알고리즘: 다익스트라
# 아이디어: X를 시작 노드로 한 다익스트라 & 모든 간선들의 방향을 바꾼 후 X를 시작 노드로 하는 다익스트라
import sys, heapq
input = sys.stdin.readline
INF = float('inf')

N, M, X = map(int, input().split())
graph = {v: [] for v in range(1, N + 1)}
reversed_graph = {v: [] for v in range(1, N + 1)} # 간선들의 방향을 바꾼 그래프
for _ in range(M): # 단방향 그래프
  s, e, t = map(int, input().split())
  graph[s].append((e, t))
  reversed_graph[e].append((s, t))

def dijkstra(start, graph):
  q = [(0, start)]
  d = [INF] * (N + 1)
  d[X] = 0
  
  while q:
    dist, node = heapq.heappop(q)
    if d[node] < dist: continue    
    for new_node, new_dist in graph[node]:
      if d[new_node] > dist + new_dist:
        d[new_node] = dist + new_dist # 갱신
        heapq.heappush(q, (dist + new_dist, new_node))
  
  return d

distance = dijkstra(X, graph) # 원래 그래프 다익스트라
reversed_distance = dijkstra(X, reversed_graph) # 방향을 바꾼 그래프 다익스트라

max_time = 0
for i in range(1, N + 1):
  if distance[i] + reversed_distance[i] > max_time:
    max_time = distance[i] + reversed_distance[i]

print(max_time)