# https://www.acmicpc.net/problem/14938

# 내 답안
# 걸린 시간: 40ms
# 알고리즘: 다익스트라
import sys, heapq
input = sys.stdin.readline
INF = float('inf')

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = {v: [] for v in range(1, n + 1)}
for _ in range(r): # 양방향 그래프
  a, b, l = map(int, input().split())
  graph[a].append((b, l))
  graph[b].append((a, l))

def dijkstra(start):
  count = 0 # 이번 다익스트라를 통해 얻을 수 있는 아이템 개수
  distance = [INF] * (n + 1)
  distance[start] = 0
  
  q = [(0, start)] # (거리, 노드)
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist: continue # 갱신할 필요가 없으면 pass
    for new_node, new_dist in graph[now]:
      if distance[new_node] > dist + new_dist:
        distance[new_node] = dist + new_dist
        heapq.heappush(q, (dist + new_dist, new_node))
  
  for i in range(1, n + 1):
    if distance[i] <= m: count += items[i]
  
  return count

max_items = 0 # 최대 아이템 개수
for node in range(1, n + 1):
  answer = dijkstra(node)
  max_items = max(max_items, answer) # 갱신

print(max_items)