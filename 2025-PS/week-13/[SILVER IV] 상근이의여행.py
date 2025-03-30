# https://www.acmicpc.net/problem/9372

# 내 답안
# DFS로 풀었는데 시간초과/메모리초과 나서 질문 게시판을 보니 기획 의도가 있었다 ...!
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(start, count):
  global graph, min_count, visited

  if all(x for x in visited): 
    min_count = min(min_count, count)
    return 
  for node in graph[start]:
    if not visited[node-1]:
      visited[node-1] = True
      dfs(node, count+1)
      visited[node-1] = False

T = int(input().strip())
for _ in range(T):
  N, M = map(int, input().strip().split())
  graph = dict()
  for _ in range(M):
    s, e = map(int, input().strip().split())
    graph[s] = graph.get(s, []) + [e] 
    graph[e] = graph.get(e, []) + [s]

  min_count = float('inf') # 제출할 정답
  visited = [False] * (N)
  for i in range(1, N+1):
    visited[i-1] = True
    dfs(i, 0)
    visited[i-1] = False
  print(min_count)

# 통과 코드
# 걸린 시간: 404ms
# N개의 노드를 가진 어떤 연결 그래프에서 모든 노드를 연결하는 최소 간선 개수는 항상 N-1이다 (!)
import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
  N, M = map(int, input().strip().split())
  graph = dict()
  for _ in range(M):
    s, e = map(int, input().strip().split())
    graph[s] = graph.get(s, []) + [e] 
    graph[e] = graph.get(e, []) + [s]
  print(N-1)