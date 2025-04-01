# https://www.acmicpc.net/problem/13549

# 내 답안
# 걸린 시간: 132ms
# 다익스트라 알고리즘을 사용 (!)
import heapq

INF = 1e8
N, K = map(int, input().split())

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start)) # (걸리는 시간, 노드)
  distance = [INF] * 100001 # 1번 노드부터 시작
  distance[start] = 0 # 현재 노드의 시간은 0
  
  left, right = 0, 100000
  while q:
    time, node = heapq.heappop(q)
    if node == K: # 목적지에 도달하면 최소 시간 반환
      return time

    if distance[node] < time: continue # 최소 시간이 아니라면 pass
    if (left <= node-1 <= right) and (distance[node-1] > time+1):
      distance[node-1] = time+1
      heapq.heappush(q, (time+1, node-1))
    if (left <= node+1 <= right) and (distance[node+1] > time+1):
      distance[node+1] = time+1
      heapq.heappush(q, (time+1, node+1))
    if (left <= node*2 <= right) and (distance[node*2] > time):
      distance[node*2] = time
      heapq.heappush(q, (time, node*2))

print(dijkstra(N))