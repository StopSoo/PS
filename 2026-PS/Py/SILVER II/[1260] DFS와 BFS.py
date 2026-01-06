# https://www.acmicpc.net/problem/1260
# 260106 풀이
# 알고리즘: DFS, BFS
# 시간:

import sys
input = sys.stdin.readline

from collections import deque, defaultdict

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

N, M, start = map(int, input().strip().split())
dt = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().strip().split())
    dt[a].append(b)
    dt[b].append(a)

checked = [False for _ in range(N + 1)]
dfs(start)
print()

checked = [False for _ in range(N + 1)]
bfs(start)
print()