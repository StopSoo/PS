# https://www.acmicpc.net/problem/12851

# 내 답안
# 걸린 시간: 268ms
# 다익스트라 알고리즘을 활용 (!)
# 막혔던 부분 1) TypeError -> 정답을 도출하는 부분이 아니어도 반환값은 있어야 함 (!)
# 막혔던 부분 2) count 체크 -> 13549_숨바꼭질3 문제와 다른 부분이기도 함. 등호 포함 여부 (!)
import heapq

INF = 1e8
N, K = map(int, input().split())

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start)) # (걸리는 시간, 노드)
  distance = [INF] * 100001 # 1번 노드부터 시작
  distance[start] = 0 # 현재 노드의 시간은 0

  left, right = 0, 100000
  count = 0 # 가장 빠른 시간으로 동생을 찾는 방법의 수
  min_time = 0
  while q:
    time, node = heapq.heappop(q)
    if node == K: # 목적지에 도달하면 최소 시간 반환
      min_time = time
      count += 1
    if min_time != 0 and time > min_time: # 정답 반환
      return (min_time, count)
    
    if distance[node] < time: continue # 최소 시간이 아니라면 pass
    # 현재 저장되어 있는 값과 같더라도 힙에 추가 (!)
    if (left <= node-1 <= right) and (distance[node-1] >= time+1):
      distance[node-1] = time+1
      heapq.heappush(q, (time+1, node-1))
    if (left <= node+1 <= right) and (distance[node+1] >= time+1):
      distance[node+1] = time+1
      heapq.heappush(q, (time+1, node+1))
    if (left <= node*2 <= right) and (distance[node*2] >= time+1):
      distance[node*2] = time+1    
      heapq.heappush(q, (time+1, node*2))
  return (min_time, count) # 기본값 반환

result = dijkstra(N)
print(result[0])
print(result[1])

# 다른 사람의 답안
# 걸린 시간: 160ms
# dist, count를 모두 배열로 한 것 좋은 것 같음.
from collections import deque

N, K = map(int, input().split())
dist = [-1] * 100001 # 최소 시간
count = [0] * 100001 # 경우의 수
queue = deque()
queue.append(N)
dist[N] = 0
count[N] = 1

while queue:
  current = queue.popleft()
  for next_pos in (current - 1, current + 1, current * 2):
    if 0 <= next_pos < 100001:
      if dist[next_pos] == -1:
        dist[next_pos] = dist[current] + 1
        count[next_pos] = count[current]
        queue.append(next_pos)
      elif dist[next_pos] == dist[current] + 1:
        count[next_pos] += count[current]

print(dist[K]) 
print(count[K])