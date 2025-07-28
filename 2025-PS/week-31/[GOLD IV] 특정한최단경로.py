# https://www.acmicpc.net/problem/1504

# 내 답안
# 걸린 시간: 516ms
import sys, heapq
input = sys.stdin.readline
INF = float('inf')

N, E = map(int, input().split())
graph = {v: [] for v in range(1, N + 1)}
for _ in range(E):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))
v1, v2 = map(int, input().split()) # 꼭 거쳐야 하는 정점의 번호

# 1번 노드에서 다익스트라
dist_1 = [INF] * (N + 1)
dist_1[1] = 0
q = [(0, 1)] # (거리, 노드)
while q:
  weight, node = heapq.heappop(q)
  if dist_1[node] < weight: continue
  for new_node, new_dist in graph[node]:
    if dist_1[new_node] > weight + new_dist: # 갱신이 필요한 경우에만 체크
      dist_1[new_node] = weight + new_dist
      heapq.heappush(q, (dist_1[new_node], new_node))

# v1 노드에서 다익스트라
dist_v1 = [INF] * (N + 1)
dist_v1[v1] = 0
q = [(0, v1)] # (거리, 노드)
while q:
  weight, node = heapq.heappop(q)
  if dist_v1[node] < weight: continue
  for new_node, new_dist in graph[node]:
    if dist_v1[new_node] > weight + new_dist: # 갱신이 필요한 경우에만 체크
      dist_v1[new_node] = weight + new_dist
      heapq.heappush(q, (dist_v1[new_node], new_node))

# v2 노드에서 다익스트라
dist_v2 = [INF] * (N + 1)
dist_v2[v2] = 0
q = [(0, v2)] # (거리, 노드)
while q:
  weight, node = heapq.heappop(q)
  if dist_v2[node] < weight: continue
  for new_node, new_dist in graph[node]:
    if dist_v2[new_node] > weight + new_dist: # 갱신이 필요한 경우에만 체크
      dist_v2[new_node] = weight + new_dist
      heapq.heappush(q, (dist_v2[new_node], new_node))

result1 = dist_1[v1] + dist_v1[v2] + dist_v2[N]
result2 = dist_1[v2] + dist_v2[v1] + dist_v1[N]
answer = min(result1, result2)
print(answer if answer < INF else -1)

# 개선 버전(함수 구현)
# 걸린 시간: 368ms
import sys, heapq
input = sys.stdin.readline
INF = float('inf')

N, E = map(int, input().split())
graph = {v: [] for v in range(1, N + 1)}
for _ in range(E):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))
v1, v2 = map(int, input().split()) # 꼭 거쳐야 하는 정점의 번호

def dijkstra(start):
  distance = [INF] * (N + 1)
  q = []
  heapq.heappush(q, (0, start)) # (거리, 노드)
  distance[start] = 0

  while q:
    dist, node = heapq.heappop(q)
    if distance[node] < dist: continue    
    for new_node, new_dist in graph[node]:
      if distance[new_node] > dist + new_dist:
        distance[new_node] = dist + new_dist
        heapq.heappush(q, (dist + new_dist, new_node))
  
  return distance

# 다익스트라를 3번 수행
dist_1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

# 두 가지 경로에 대해 계산 후 최단 경로 찾기
result1 = dist_1[v1] + dist_v1[v2] + dist_v2[N]
result2 = dist_1[v2] + dist_v2[v1] + dist_v1[N]
answer = min(result1, result2)

# 최단 경로가 없을 경우 -1을 출력
print(answer if answer < INF else -1)