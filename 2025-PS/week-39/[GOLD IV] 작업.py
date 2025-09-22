# https://www.acmicpc.net/problem/2056

# 내 답안
# 걸린 시간: 384ms
# 알고리즘: 위상 정렬
import sys, heapq
input = sys.stdin.readline

N = int(input().strip())
graph = [[] for _ in range(N + 1)]
times = [0] * (N + 1) # 작업에 걸리는 시간
plus = [0] * (N + 1) # 추가로 더해지는 시간
indegree = [0] * (N + 1) # 진입 차수
for i in range(1, N + 1):
  l = list(map(int, input().strip().split()))
  times[i] = l[0]
  indegree[i] = l[1]
  for j in range(l[1]):
    graph[l[j+2]].append(i)

hq = []
for i in range(1, N + 1):
  if indegree[i] == 0:
    heapq.heappush(hq, (0, i))
while hq:
  prev, now = heapq.heappop(hq)
  if prev != 0:
    times[now] += plus[now]
  for nxt in graph[now]:
    indegree[nxt] -= 1
    plus[nxt] = max(plus[nxt], times[now]) # 더해져야 하는 최대 시간 찾기 (!)
    if indegree[nxt] == 0:
      heapq.heappush(hq, (now, nxt))

print(max(times))