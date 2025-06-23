# https://www.acmicpc.net/problem/15900

# 내 답안
# 걸린 시간: 1880ms
# 알고리즘: DFS
import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(1000000)

N = int(input())
graph = defaultdict(list)
for _ in range(N-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (N + 1)
total_dist = 0
def dfs(node, depth):
  global total_dist  
  visited[node] = True     
  is_leaf = True   

  for neighbor in graph[node]:
    if not visited[neighbor]:
      is_leaf = False              
      dfs(neighbor, depth + 1)
  
  if is_leaf: # 리프노드일 때만 누적시키기(!)
    total_dist += depth

dfs(1, 0)
print("Yes" if total_dist % 2 == 1 else "No")