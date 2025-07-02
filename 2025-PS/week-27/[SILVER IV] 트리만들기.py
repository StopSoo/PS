# https://www.acmicpc.net/problem/14244

# 내 답안
# 걸린 시간: 36ms
# 자료구조: 트리
# 트리의 성질을 잘 생각해보자! -> 쭉 연결해놓고 리프 노드 개수에 맞춰서 마지막 노드에 연결하는 방식.
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = []
last_path_node = n - m
for i in range(last_path_node):
  edges.append((i, i + 1))

current_node = last_path_node + 1
for _ in range(m - 1):
  edges.append((last_path_node, current_node))
  current_node += 1
# 출력
for u, v in edges:
  print(u, v)