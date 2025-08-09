# https://www.acmicpc.net/problem/1325

# 내 답안
# 걸린 시간: 12188ms(pypy3)
# 알고리즘: 그래프 탐색
# 원래 코드: 모든 노드에서 BFS를 돌림 -> 매우 느림 (그래도 pypy3로 통과)
# 개선 코드: DFS + 메모이제이션 -> 근데 백준에서는 시간/메모리초과 남 ... 뭐지
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
  a, b = map(int, input().strip().split())
  graph[b].append(a) # 단방향 그래프

def dfs(node, visited):
  visited[node] = True
  count = 1 # 시작 컴퓨터
  for nxt in graph[node]:
    if not visited[nxt]:
      count += dfs(nxt, visited)
  return count

max_cnt = 0
ans = [] # 해킹 컴퓨터의 수가 최대인 컴퓨터들의 번호
for i in range(1, N + 1):
  visited = [False] * (N + 1)
  c = dfs(i, visited)
  if c > max_cnt:
    max_cnt = c
    ans = [i]
  elif c == max_cnt:
    ans.append(i)

print(*ans)

# 최종 개선 코드
# 걸린 시간: 10148ms(pypy3)
# 거의 비슷하지만 count를 sum으로 체크하지 않는다는 등의 자잘한 포인트들이 다름.
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  a, b = map(int, input().split())
  graph[b].append(a)

def bfs(start):
  visited = [False] * (N+1)
  visited[start] = True
  q = deque([start])
  count = 1
  while q:
    node = q.popleft()
    for nxt in graph[node]:
      if not visited[nxt]:
        visited[nxt] = True
        q.append(nxt)
        count += 1
  return count

max_count = 0
result = []
for i in range(1, N+1):
  cnt = bfs(i)
  if cnt > max_count:
    max_count = cnt
    result = [i]
  elif cnt == max_count:
    result.append(i)

print(*result)