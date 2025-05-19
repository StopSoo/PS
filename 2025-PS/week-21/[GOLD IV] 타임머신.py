# https://www.acmicpc.net/problem/11657

# 답안
# 걸린 시간: 752ms
# 알고리즘: 벨만-포드 알고리즘(음수 가중치를 갖는 간선이 존재할 때)
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().strip().split()) # 도시, 버스
edges = [] # 모든 간선에 대한 정보를 담는 리스트
distance = [INF] * (N+1)

for _ in range(M):
  s, e, t = map(int, input().strip().split())
  edges.append((s, e, t))

def bf(start):
  distance[start] = 0 # 시작 노드의 최단 거리는 0
  for i in range(N):
    for j in range(M): # 매 반복마다 모든 간선을 확인 (!)
      cur_node = edges[j][0]
      next_node = edges[j][1]
      edge_cost = edges[j][2]
      # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
      if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + edge_cost:
        distance[next_node] = distance[cur_node] + edge_cost # 갱신
        if i == N - 1: # N번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
          return True
  return False

# 벨만포드 알고리즘 수행
negative_cycle = bf(1) # 1번 노드에서 시작

if negative_cycle: print("-1")
else: # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리를 출력
  for i in range(2, N+1):
    print(distance[i] if distance[i] != INF else "-1")