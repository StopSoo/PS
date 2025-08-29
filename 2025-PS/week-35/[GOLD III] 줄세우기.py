# https://www.acmicpc.net/problem/2252

# 내 답안
# 걸린 시간: 196ms
# 알고리즘: 위상정렬
import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().strip().split())
indegree = [0] * (N + 1)
graph = [[] for i in range(N + 1)]
for _ in range(M):
  a, b = map(int, input().strip().split())
  graph[a].append(b)
  indegree[b] += 1

hq = []
answer = []
for i in range(1, N + 1):
  if indegree[i] == 0:
    heapq.heappush(hq, i)

while hq:
  now = heapq.heappop(hq)
  answer.append(now)
  for nxt in graph[now]:
    indegree[nxt] -= 1
    if indegree[nxt] == 0:
      heapq.heappush(hq, nxt)

print(*answer)