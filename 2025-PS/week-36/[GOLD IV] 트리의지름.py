# https://www.acmicpc.net/problem/1967

# 내 답안
# 걸린 시간:68ms
# 알고리즘/자료구조: 트리/그래프
# 아이디어: 루트 노드에서 DFS를 돌려 가장 먼 노드를 찾고, 그 노드에서 다시 DFS를 돌려 가장 먼 노드를 찾는다.
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node, dist):
  global graph, visited, max_dist, farthest_node
  
  visited[node] = 1 # 방문 체크
  if dist > max_dist: # 갱신 필요 시
    max_dist = dist
    farthest_node = node
  for nxt_node, nxt_weight in graph[node]:
    if not visited[nxt_node]:
      dfs(nxt_node, dist + nxt_weight)

n = int(input().strip())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(n - 1):
  p, c, w = map(int, input().strip().split())
  graph[p].append((c, w))
  graph[c].append((p, w))

if n == 1: # 예외 처리 (!)
  print(0)
  sys.exit()
# 루트 노드인 노드 1에서 DFS
visited = [0] * (n + 1)
max_dist = 0 # 최장 거리
farthest_node = 0 # 루트 노드로부터 최장 거리에 있는 노드 번호
dfs(1, 0)
# 루트 노드에서 가장 먼 노드에서 DFS
visited = [0] * (n + 1)
max_dist = 0
dfs(farthest_node, 0)
# 정답 출력
print(max_dist)