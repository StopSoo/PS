# https://www.acmicpc.net/problem/1766

# 내 답안(복습)
# 걸린 시간: 176ms
# 알고리즘: 위상 정렬
import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().strip().split())
indegree = [0] * (N + 1) # 모든 노드에 대한 진입 차수는 0으로 초기화
graph = [[] for i in range(N + 1)]

for _ in range(M):
  a, b = map(int, input().strip().split())
  graph[a].append(b) # a를 b보다 먼저 풀어야 함
  indegree[b] += 1
# 위상 정렬 함수
def topology_sort():
  result = []
  hq = []
  # 처음 시작할 때는 진입 차수가 0인 노드들을 큐에 삽입
  for i in range(1, N + 1):
    if indegree[i] == 0:
      heapq.heappush(hq, i)
  # 큐가 빌 때까지 반복
  while hq:
    now = heapq.heappop(hq)
    result.append(now)
    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        heapq.heappush(hq, i)
  # 위상 정렬을 수행한 결과 출력
  print(*result)

topology_sort()