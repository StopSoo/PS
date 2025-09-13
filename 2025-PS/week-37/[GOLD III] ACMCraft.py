# https://www.acmicpc.net/problem/1005

# 내 답안
# 걸린 시간: 956ms
# 알고리즘: 위상 정렬
# 같은 유형의 1516_게임 개발 문제 코드 참고해서 품!
import sys, heapq
input = sys.stdin.readline

def topology_sort():
  result = [0] * (N + 1)
  hq = []

  for i in range(1, N + 1):
    if indegrees[i] == 0:
      heapq.heappush(hq, (i, times[i]))
  
  while hq:
    now, time = heapq.heappop(hq)
    result[now] = time
    for nxt in graph[now]:
      indegrees[nxt] -= 1
      result[nxt] = max(result[nxt], result[now] + times[nxt]) # 핵심(!!!)
      if indegrees[nxt] == 0:
        heapq.heappush(hq, (nxt, result[nxt]))

  return result

T = int(input().strip())
for _ in range(T):
  N, K = map(int, input().strip().split())
  times = [0] + list(map(int, input().strip().split()))
  indegrees = [0] * (N + 1) # 진입 차수
  graph = [[] for _ in range(N + 1)]
  for _ in range(K): # 규칙
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    indegrees[b] += 1
  building = int(input())

  result = topology_sort()
  print(result[building])