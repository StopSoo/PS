# https://www.acmicpc.net/problem/11779

# 내 답안
# 걸린 시간: 328ms
# 알고리즘: 다익스트라 & 역추적(!)
# 최적화 방식
# 1) 내가 처음에 작성한 방식처럼 경로를 힙에 넣고 반복해서 복사하는 것은 비효율적이며, 시간 초과를 유발한다(!)
# 2) 경로는 prev 배열을 이용해 나중에 복원한다.
import sys, heapq
from collections import defaultdict
input = sys.stdin.readline
INF = float('inf')

n = int(input().strip())
m = int(input().strip())
graph = defaultdict(list)
for _ in range(m):
  s, e, w = map(int, input().strip().split())
  graph[s].append((e, w))
start, end = map(int, input().strip().split())
# 다익스트라 
dist = [INF] * (n + 1)
dist[start] = 0
prev = [0] * (n + 1) # 경로 추적용(!)
hq = [(0, start)] # (비용, 현재 노드)
while hq:
  weight, now = heapq.heappop(hq)

  if dist[now] < weight: continue
  for nxt_node, nxt_weight in graph[now]:
    if weight + nxt_weight < dist[nxt_node]:
      dist[nxt_node] = weight + nxt_weight
      prev[nxt_node] = now
      heapq.heappush(hq, (weight + nxt_weight, nxt_node))
# 역추적을 통한 최종 경로 찾기(!)
route = []
cur = end 
while cur:
  route.append(cur)
  cur = prev[cur]
route.reverse()
# 최소 비용
print(dist[end])
# 경로에 포함된 도시 개수
print(len(route))
# 최소 비용을 갖는 경로
print(*route)