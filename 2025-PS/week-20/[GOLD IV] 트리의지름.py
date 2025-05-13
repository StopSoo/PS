# https://www.acmicpc.net/problem/1967

# 답안
# 걸린 시간:
# 첫 내 답안의 문제점 1) 모든 노드 조합에 대해 계산하려고 함. -> 시간 초과 발생.
# 문제점 2) DFS 종료 조건이 이상함.
# 문제점 3) 외부에 변수를 두고 값을 누적하는 방식보다는, dfs 함수 내 매개변수로 값을 전달하는 편이 나음!
# 개선점) 두 번의 DFS를 통해 시간 초과를 방지하고 정답을 효율적으로 찾을 수 있음 !!
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
graph = {i: [] for i in range(1, N + 1)}
for _ in range(N-1):
  u, v, w = map(int, input().strip().split())
  graph[u].append((v, w))
  graph[v].append((u, w))

if N == 1: # 노드 하나면 지름은 0 (꼭 체크!)
  print(0)  
  sys.exit()
# 첫 DFS: 루트(1)에서 가장 먼 노드 찾기
visited = [False] * (N + 1)
max_dist = 0
farthest_node = 0
dfs(1, 0)
# 두 번째 DFS: 가장 먼 노드에서 다시 가장 먼 거리 찾기
visited = [False] * (N + 1)
max_dist = 0
dfs(farthest_node, 0)

print(max_dist)