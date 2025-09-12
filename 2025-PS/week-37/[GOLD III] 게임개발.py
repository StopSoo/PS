# https://www.acmicpc.net/problem/1516

# 내 답안
# 걸린 시간: 64ms
# 알고리즘: 위상 정렬
# 초기 코드의 문제점: 어떤 건물이 여러 개의 선행 건물을 가질 경우를 반영하지 않았음(!)
# line36에서 max를 사용하는 이유: 여러 부모 중 가장 오래 걸리는 경로를 고려해야 하기 때문.
import sys, heapq
input = sys.stdin.readline

N = int(input().strip())
indegree = [0] * (N + 1) # 모든 노드들의 진입 차수는 0으로 초기화
graph = [[] for _ in range(N + 1)]
times = [0] * (N + 1) # 각 건물을 짓는 데 걸리는 시간

for i in range(1, N + 1):
  values = list(map(int, input().strip().split()))
  times[i] = values[0]
  if values[1] != -1:
    for j in range(1, len(values) - 1):
      indegree[i] += 1
      graph[values[j]].append(i)

def topology_sort():
  result = [0] * (N + 1) # 각 건물이 완성되기까지 걸리는 최소 시간
  hq = []

  for i in range(1, N + 1):
    if indegree[i] == 0:
      heapq.heappush(hq, (i, times[i]))
  
  while hq:
    now, time = heapq.heappop(hq)
    result[now] = time
    for nxt in graph[now]: 
      indegree[nxt] -= 1 
      result[nxt] = max(result[nxt], result[now] + times[nxt]) # 핵심(!!!)
      if indegree[nxt] == 0: 
        heapq.heappush(hq, (nxt, result[nxt]))

  return result[1:]

result = topology_sort()
for i in range(len(result)): print(result[i])