# https://www.acmicpc.net/problem/11724

# 내 답안
# 걸린 시간: 632ms (무조건 빠른 입출력 사용해야 함!)
# 일단 가장 큰 문제는 이 문제를 보고 dfs / bfs를 사용할 생각을 못했다는 것. -> dfs / bfs 문제와 익숙해져야 할 듯
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(v, visited):
  visited[v] = True
  for g in graph[v]:
    if not visited[g]: dfs(g, visited)
  return 1

N, M = map(int, input().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  u, v = map(int, input().strip().split())
  graph[u].append(v)
  graph[v].append(u)

visited = [False for _ in range(N+1)] # 방문 배열
count = 0
for i in range(1, N+1):
  if not visited[i]:
    count += dfs(i, visited)
print(count)