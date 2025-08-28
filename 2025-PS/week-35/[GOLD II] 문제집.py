# https://www.acmicpc.net/problem/1766

# 내 답안
# 걸린 시간: 188ms(python3)
# 아이디어: 순서대로 풀되, 먼저 풀어야 하는 문제가 있는 문제의 경우 일단 패스.
# 알고리즘: 대표적인 "위상 정렬" 문제 (!)

# 주의사항
# 1) “가능하면 쉬운 문제부터”는 진입 차수가 0인 문제들 중에서 최소 번호 선택이라는 의미
# 2) 단순히 연결된 노드만 정렬한다고 해결되지 않음
# 3) 여러 노드가 동시에 진입 차수 0이 될 때 우선순위 선택이 결과를 결정
import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().strip().split())
indegree = [0] * (N + 1) # 모든 노드에 대한 진입 차수는 0으로 초기화
graph = [[] for i in range(N + 1)]

for _ in range(M):
  a, b = map(int, input().strip().split())
  graph[a].append(b) # a를 b보다 먼저 풀어야 함
  indegree[b] += 1 # b의 진입 차수 1 증가
# 위상정렬
def topology_sort():
  result = []
  hq = []
  # 처음 시작할 때는 진입 차수가 0인 노드들을 큐에 삽임
  for i in range(1, N + 1):
    if indegree[i] == 0: heapq.heappush(hq, i)
  # 큐가 빌 때까지 반복
  while hq:
    now = heapq.heappop(hq)
    result.append(now)
    # 해당 원소와 연결된 노드들의 진입 차수에서 1 빼기
    for i in graph[now]:
      indegree[i] -= 1
      # 새롭게 진입 차수가 0이 되었다면 노드를 큐에 삽입
      if indegree[i] == 0:
        heapq.heappush(hq, i)
  # 위상 정렬을 수행한 결과 출력
  print(*result)

topology_sort()