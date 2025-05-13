# https://www.acmicpc.net/problem/1167

# 내 답안
# 걸린 시간: 932ms
# 1967번과 거의 같은 문제. 입출력 받는 것만 다름 (!)
# 트리의 지름 핵심 아이디어) 아무 정점에서 시작해 DFS/BFS로 가장 먼 노드를 찾고, 그 노드에서 다시 DFS/BFS로 가장 먼 거리를 찾는다.
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(node, dist):
  global max_dist, farthest_node

  visited[node] = True   
  if dist > max_dist: # 갱신
    max_dist = dist
    farthest_node = node
  for neighbor, weight in graph[node]:
    if not visited[neighbor]:
      dfs(neighbor, dist + weight)

N = int(input())
graph = {i: set() for i in range(1, N+1)}
for _ in range(N):
  l = list(map(int, input().strip().split()))
  ind = 1
  while True:
    if l[ind] != -1:
      graph[l[0]].add((l[ind], l[ind+1]))
      graph[l[ind]].add((l[0], l[ind+1]))
      ind += 2
    else: break

if N == 1: # 노드 하나면 지름은 0
  print(0)
  sys.exit()
# 첫 DFS: 루트(1이라고 가정)에서 가장 먼 노드 찾기
visited = [False] * (N + 1)
max_dist = 0
farthest_node = 0
dfs(1, 0)
# 두 번째 DFS: 가장 먼 노드에서 다시 가장 먼 거리 찾기
visited = [False] * (N + 1)
max_dist = 0
dfs(farthest_node, 0)

print(max_dist)