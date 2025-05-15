# https://www.acmicpc.net/problem/1916

# 내 답안 1
# 일반적인 BFS -> 시간 초과 남 !!
import sys
input = sys.stdin.readline
from collections import deque

N = int(input()) # 노드
M = int(input()) # 간선
graph = {i: [] for i in range(1, N+1)}
for _ in range(M):
  u, v, w = map(int, input().strip().split())
  graph[u].append((v, w))
s, e = map(int, input().strip().split())

min_dist = float('inf')
visited = [False] * (N+1)
deq = deque()
deq.append((s, e, 0))
while deq:
  start, end, dist = deq.popleft()
  if start == end:
    min_dist = min(min_dist, dist) # 갱신

  visited[start] = True # 방문 체크
  for neighbor, w in graph[start]:
    if not visited[neighbor]:
      deq.append((neighbor, end, dist + w))

print(min_dist)

# 내 답안 2
# 걸린 시간: 다익스트라 사용 -> 284ms
# 뒤늦게 발견한 문제점: 방향 그래프인데 무방향 그래프로 구현함;
import sys, heapq
input = sys.stdin.readline

N = int(input()) # 노드
M = int(input()) # 간선
graph = {i: [] for i in range(1, N+1)}
for _ in range(M):
  u, v, w = map(int, input().strip().split())
  graph[u].append((v, w))
s, e = map(int, input().strip().split())
dist = [float('inf')] * (N+1) # 최소 비용 배열 (다익스트라의 핵심!)

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, s)) # (누적 가중치, 노드)
  dist[s] = 0

  while q:
    weight, now = heapq.heappop(q)
    if dist[now] < weight: continue

    for next_node, next_w in graph[now]: # 연결된 모든 노드 탐색
      if weight + next_w < dist[next_node]:
        dist[next_node] = weight + next_w # 갱신
        heapq.heappush(q, (weight + next_w, next_node)) # (누적 가중치, 노드)

dijkstra(s)
print(dist[e])