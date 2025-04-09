# https://www.acmicpc.net/problem/1446

# 내 답안
# 걸린 시간: 36ms
# 대충 어떤 느낌으로 풀어야 하는지 알겠는데 ~ 완성을 못 함
# DP 풀이
import sys
input = sys.stdin.readline

N, D = map(int, input().strip().split())  
dp = [i for i in range(D+1)]

graph = []
for _ in range(N):
  s, e, length = map(int, input().strip().split())
  if e - s > length: # 지름길인 경우만 추가
    graph.append((s, e, length))
graph.sort() # 정렬 필수 !!

for s, e, dist in graph:
  for i in range(1, D+1):
    if i == e:
      dp[i] = min(dp[i], dp[s] + dist) # dp[s]+dist가 킥입니다요
    else:
      dp[i] = min(dp[i], dp[i-1] + 1)

print(dp[D])

# 다익스트라 풀이
import sys, heapq

n, d = map(int, sys.stdin.readline().split())
inf = float("inf")

graph = [[] for _ in range(d+1)]
dist = [inf] * (d+1)

for i in range(d):
  graph[i].append((i+1, 1)) # 모든 노드의 기본 가중치는 1

for _ in range(n):
  start, dest, length = map(int, sys.stdin.readline().split())
  if dest <= d:
    graph[start].append((dest, length))

q = []
heapq.heappush(q, (0, 0))
dist[0] = 0

while q:
  w1, u = heapq.heappop(q)

  for v, w2 in graph[u]:
    cost = dist[u] + w2
    if dist[v] > cost:
      dist[v] = cost # 갱신
      heapq.heappush(q, (cost, v))

print(dist[d])