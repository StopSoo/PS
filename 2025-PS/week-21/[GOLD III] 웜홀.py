# https://www.acmicpc.net/problem/1865

# 답안
# 걸린 시간: 928ms
# 주의할 점 1) 11657_타임머신 문제와 다르게 시작 노드가 지정되어 있지 않음. 
# 주의할 점 2) "도로는 방향이 없으며, 웜홀은 방향이 있음"
# 아이디어) "가상의 0번 노드": 새로운 노드 0번을 만들고, 모든 정점 1~N에 대해 0->i 간선을 추가하면, 모든 노드가 하나의 그래프에서 연결된다.
# 따라서 한번의 벨만포드 알고리즘 순회로 음수 사이클 존재 여부를 파악할 수 있다 (!)
import sys
input = sys.stdin.readline

def bf():
  distance = [0] * (N + 1) # 가상의 시작점(0)에서 모든 노드까지의 거리를 0으로 초기화
  for i in range(N):
    for cur_node, next_node, edge_cost in edges: # 매 반복마다 모든 간선을 확인 (!)
      # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 갱신
      if distance[next_node] > distance[cur_node] + edge_cost:
        distance[next_node] = distance[cur_node] + edge_cost
        if i == N-1: # N번째 라운드에서도 값이 갱신된다면 음수 순환이 존재.
          return True 
  return False

TC = int(input())
for _ in range(TC):
  N, M, W = map(int, input().strip().split()) # 지점, 도로, 웜홀
  edges = [] # 모든 간선에 대한 정보를 담는 리스트

  for _ in range(M): # 도로
    s, e, t = map(int, input().strip().split())
    edges.append((s, e, t))
    edges.append((e, s, t))
  for _ in range(W): # 웜홀
    s, e, t = map(int, input().strip().split())
    edges.append((s, e, -t))
  # 0번 노드에 대해 벨만포드 알고리즘을 한 번만 수행 (!)
  if bf(): print("YES")
  else: print("NO")