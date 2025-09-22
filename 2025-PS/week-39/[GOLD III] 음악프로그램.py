# https://www.acmicpc.net/problem/2623

# 내 답안
# 걸린 시간: 68ms
# 알고리즘: 위상 정렬
# 문제를 꼼꼼히 읽어라 ... 그리고 예외 조건을 잘 체크해라 ...
import sys, heapq
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().strip().split())
graph = defaultdict(list)
indegrees = [0] * (N + 1) # 진입 차수 기록
for _ in range(M):
  lis = list(map(int, input().strip().split()))
  for i in range(1, lis[0]):
    graph[lis[i]].append(lis[i+1])
    indegrees[lis[i+1]] += 1

def topology_sort():
  result = []
  hq = []
  for i in range(1, N + 1):
    if indegrees[i] == 0:
      heapq.heappush(hq, i)

  while hq:
    now = heapq.heappop(hq)
    result.append(now)
    for nxt in graph[now]:
      indegrees[nxt] -= 1
      if indegrees[nxt] == 0:
        heapq.heappush(hq, nxt)
  
  if len(result) == N: print(*result, sep='\n')
  else: print(0)

topology_sort()