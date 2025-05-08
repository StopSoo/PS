# https://www.acmicpc.net/problem/1753

# 내 답안
# 걸린 시간: 648ms
# 시간 초과, 메모리 초과 다 났었던 첫 코드 ..
# 결론은 deque, pq 필요 없고 heapq를 사용해라 ~ 
import sys
input = sys.stdin.readline
import heapq

V, E = map(int, input().strip().split())
start = int(input())
graph = {v: [] for v in range(1, V+1)}
for _ in range(E):
  u, v, w = map(int, input().strip().split())
  graph[u].append((w, v)) # (거리, 종점)

q = []
heapq.heappush(q, (0, start))
weights = [float('inf')] * (V+1) # 1 기반 인덱스
weights[start] = 0 # 시작점의 가중치는 0
while q:
  w, node = heapq.heappop(q)
  if weights[node] < w: continue # 방문 체크 (중요!!!!!!!)
  for next_w, next_node in graph[node]:
    if weights[next_node] > w + next_w: # 더 작은 값이 나올 때만
      weights[next_node] = w + next_w # 갱신
      heapq.heappush(q, (w + next_w, next_node))

for weight in weights[1:]:
  if weight == float('inf'): print("INF")
  else: print(weight)