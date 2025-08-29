# https://www.acmicpc.net/problem/14567

# 내 답안
# 걸린 시간: 596ms
# 알고리즘: 위상정렬
# 처음에 메모리 초과 난 이유 -> 진입 차수가 0이 아닐 때도 힙에 원소를 넣어서!!
# 문제가 막혔을 때 해결할 수 있었던 방법 -> (노드 번호, 순서)의 순서를 반대로 바꿔서 적용한 점.
import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().strip().split())
indegree = [0] * (N + 1) # 모든 노드에 대한 진입 차수 
graph = [[] for i in range(N + 1)]
for _ in range(M):
  a, b = map(int, input().strip().split())
  graph[a].append(b) # a를 b보다 먼저 수강해야 함
  indegree[b] += 1
# 위상정렬
def topology_sort():
  result = [0] * (N + 1)
  hq = []
  # 처음 시작할 때는 진입 차수가 0인 노드들을 큐에 삽입
  for i in range(1, N + 1):
    if indegree[i] == 0:
      heapq.heappush(hq, (1, i)) # (순서, 노드 번호)
  # 큐가 빌 때까지 반복
  while hq:
    order, now = heapq.heappop(hq)
    result[now] = order
    # 해당 원소와 연결된 노드들의 진입 차수에서 1 빼기
    for nxt in graph[now]:
      indegree[nxt] -= 1
      if indegree[nxt] == 0:
        heapq.heappush(hq, (order + 1, nxt))
  
  print(*result[1:])

topology_sort()