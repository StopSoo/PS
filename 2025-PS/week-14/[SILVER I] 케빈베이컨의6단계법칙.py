# https://www.acmicpc.net/problem/1389

# 내 답안
# 걸린 시간: 40ms
# 다익스트라 활용
import heapq
import sys
input = sys.stdin.readline

INF = 1e8
N, M = map(int, input().strip().split())
graph = dict()
for _ in range(M): # 그래프 만들기
  a, b = map(int, input().strip().split())
  graph[a] = graph.get(a, []) + [b]
  graph[b] = graph.get(b, []) + [a]

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start)) # (우선순위/거리, 노드)
  distance = [INF] * (N+1) # 1번 노드부터 시작
  distance[start] = 0 # 현재 노드의 거리는 0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist: # 이미 입력되어있는 값이 현재 노드까지의 거리보다 작다면 이미 방문한 노드
      continue
    
    for i in graph[now]:
      if dist+1 < distance[i]: # 기존에 입력된 값보다 더 작은 거리가 나온다면
        distance[i] = dist+1 # 값 갱신
        heapq.heappush(q, (dist+1, i))
  return sum(distance[1:])

results = []
for i in range(1, N+1):
  results.append(dijkstra(i))
print(results.index(min(results))+1)