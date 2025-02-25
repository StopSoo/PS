# https://www.acmicpc.net/problem/1260

# 답안
# 걸린 시간: 340ms
# dfs / bfs 개념만 알고 파이썬으로 어떻게 구현할지 감을 못 잡은 상태였음. (특히 BFS)
from collections import deque

def dfs(n):
  global dt, checked

  if checked[n]: return
  checked[n] = True

  print(n, end=' ')

  for neighbor in sorted(dt[n]):
    dfs(neighbor)

def bfs(n):
  global dt, checked

  q = deque()
  q.append(n)
  checked[n] = True

  while q:
    node = q.popleft()
    print(node, end=' ')

    for neighbor in sorted(dt[node]):
      if checked[neighbor]: continue
      q.append(neighbor)
      checked[neighbor] = True

N, M, start = map(int, input().split())
dt = dict()
for i in range(N): dt[i+1] = [] # 초기화
for _ in range(M):
  v1, v2 = map(int, input().split())
  dt[v1] += [v2]
  dt[v2] += [v1]

checked = [False for _ in range(N+1)]
dfs(start)
print()

checked = [False for _ in range(N+1)]
bfs(start)
print()