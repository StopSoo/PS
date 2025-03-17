# https://www.acmicpc.net/problem/1389

# 답안
# 걸린 시간: 60ms
# DFS->BFS 변경, 첫 코드 시간 초과 -> 모든 노드에 대해 BFS를 수행하는 것이 문제 (!)
from collections import deque

def bfs(s):
  """start 노드에서 모든 노드까지의 최단 거리 리스트 반환"""
  global N, dt

  dist = [-1] * (N+1) # 거리 저장
  dist[s] = 0
  deq = deque([s])

  while deq:
    node = deq.popleft()
    for next_node in dt[node]:
      if dist[next_node] == -1:
        dist[next_node] = dist[node] + 1
        deq.append(next_node)
  return sum(dist[1:]) # 1번부터 N번까지의 합을 반환

N, M = map(int, input().split())

dt = {i: set() for i in range(1, N+1)} # 선언과 동시에 초기화 (!)
for _ in range(M):
  a, b = map(int, input().split())
  dt[a].add(b)
  dt[b].add(a)
# 각 노드에서 BFS 한 번만 수행하여 베이컨 수를 계산
bacons = [bfs(i) for i in range(1, N+1)] 
print(bacons.index(min(bacons)) + 1)