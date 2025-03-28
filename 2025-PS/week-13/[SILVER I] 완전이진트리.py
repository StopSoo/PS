# https://www.acmicpc.net/problem/9934

# 내 답안
# 걸린 시간: 36ms
# 중위 순회
def get_tree(graph, depth):
  global tree, K
  
  if depth > K: return
  tree[depth-1].append(graph[len(graph)//2])
  get_tree(graph[:len(graph)//2], depth+1)
  get_tree(graph[len(graph)//2+1:], depth+1)

K = int(input()) # 트리의 높이
graph = list(map(int, input().split()))

tree = [[] for _ in range(K)]
get_tree(graph, 1)

for i in range(K):
  print(*tree[i])