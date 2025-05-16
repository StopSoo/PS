# https://www.acmicpc.net/problem/1238

# 내 답안
# 걸린 시간: 932ms
# 알고리즘: 다익스트라
# 1부터 N까지 모든 노드에 대해 다익스트라를 수행 후 왕복 거리 계산.
import sys, heapq
input = sys.stdin.readline
from collections import defaultdict

N, M, X = map(int, input().strip().split())
graph = defaultdict(list)
for _ in range(M):
  s, e, t = map(int, input().strip().split())
  graph[s].append((e, t))

def dijkstra(start):
  global times 

  q = []
  heapq.heappush(q, (0, start))
  times[start] = 0

  while q:
    time, now = heapq.heappop(q)
    if times[now] < time: continue

    for new_node, new_time in graph[now]:
      if time + new_time < times[new_node]: # 최단 시간 찾기
        times[new_node] = time + new_time # 갱신
        heapq.heappush(q, (time + new_time, new_node))

answer = [0] * (N+1)
for i in range(1, N+1):
  times = [float('inf')] * (N+1)
  dijkstra(i)
  if i != X: answer[i] += times[X]
  else:
    for j in range(1, N+1):
      if i != j: answer[j] += times[j]

print(max(answer[1:]))

# 더 효율적으로 하는 답안
# 걸린 시간: 68ms (!)
# 아이디어) 모든 마을 -> X: 역방향 그래프로 다익스트라 / X -> 모든 마을: 그냥 그래프로 다익스트라 (총 2번)
import sys, heapq
from collections import defaultdict

input = sys.stdin.readline
N, M, X = map(int, input().split())
graph = defaultdict(list)
reverse_graph = defaultdict(list)

for _ in range(M):
  s, e, t = map(int, input().split())
  graph[s].append((e, t))
  reverse_graph[e].append((s, t))  # 역방향 저장

def dijkstra(start, graph):
  dist = [float('inf')] * (N + 1)
  dist[start] = 0
  hq = [(0, start)]

  while hq:
    time, now = heapq.heappop(hq)
    if dist[now] < time: continue

    for nxt, t in graph[now]:
      if dist[nxt] > time + t:
        dist[nxt] = time + t
        heapq.heappush(hq, (time + t, nxt))
  return dist

# X → 모든 마을 (귀가)
go_home = dijkstra(X, graph)
# 모든 마을 → X (등교)
go_party = dijkstra(X, reverse_graph)
# 왕복 거리의 최대값 구하기
max_time = 0
for i in range(1, N+1):
  total = go_home[i] + go_party[i]
  max_time = max(max_time, total)

print(max_time)
