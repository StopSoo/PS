# https://www.acmicpc.net/problem/1504

# 내 답안
# 걸린 시간: 376ms
# 알고리즘: 다익스트라
import sys, heapq 
input = sys.stdin.readline

INF = 1e9
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
  u, v, w = map(int, input().split())
  graph[u].append((v, w))
  graph[v].append((u, w))
v1, v2 = map(int, input().split()) # 반드시 거쳐야 하는 정점 두 개

def dijkstra(start):
  distance = [INF] * (N+1)
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist: continue

    for neighbor, weight in graph[now]:
      if dist + weight < distance[neighbor]:
        distance[neighbor] = dist + weight
        heapq.heappush(q, (dist + weight, neighbor))
  
  return distance

# 다익스트라를 3번 수행
dist_1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)
# 두 경로에 대해 계산
path1 = dist_1[v1] + dist_v1[v2] + dist_v2[N]
path2 = dist_1[v2] + dist_v2[v1] + dist_v1[N]

answer = min(path1, path2)
print(answer if answer < INF else -1)