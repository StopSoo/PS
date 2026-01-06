# https://www.acmicpc.net/problem/2178
# 260106 풀이
# 알고리즘: 그래프 탐색(BFS)
# 시간: 76ms

from collections import deque
# 상하좌우 이동 좌표
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M = map(int, input().split())
miro = [list(input()) for _ in range(N)]

deq = deque()
visited = [[False] * M for _ in range(N)]
visited[0][0] = True # 시작점
deq.append((0, 0, 1)) # 시작 위치(y, x), 지난 칸 수

while deq:
    y, x, dist = deq.popleft()

    if y == N - 1 and x == M - 1:
        print(dist)
        break

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if (0 <= ny < N and 0 <= nx < M) and (not visited[ny][nx]) and (miro[ny][nx] == '1'):
            deq.append((ny, nx, dist + 1))
            visited[ny][nx] = True
