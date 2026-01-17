# https://www.acmicpc.net/problem/2667
# 260117 풀이
# 알고리즘: 그래프 탐색
# 시간: 56ms

# 첫 코드
import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
graph = [list(input().strip()) for _ in range(n)]
counts = []

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    global visited

    deq = deque([(y, x)])
    count = 0

    while deq:
        nowY, nowX = deq.popleft()
        graph[nowY][nowX] = '0'
        count += 1

        for i in range(4):
            ny, nx = nowY + dy[i], nowX + dx[i]
            if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == '1' and not visited[ny][nx]:
                deq.append((ny, nx))
                visited[ny][nx] = True
                graph[ny][nx] = '0'
    return count

visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            count = bfs(i, j)
            counts.append(count)

counts.sort()
print(len(counts))
print(*counts, sep='\n')

# 좀 더 개선된 코드
import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
graph = [list(input().strip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)] # 전역 선언 후 사용
counts = []

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    deq = deque([(y, x)])
    visited[y][x] = True # 시작점 방문 처리
    count = 1

    while deq:
        nowY, nowX = deq.popleft()

        for i in range(4):
            ny, nx = nowY + dy[i], nowX + dx[i]
            if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == '1' and not visited[ny][nx]:
                deq.append((ny, nx))
                visited[ny][nx] = True
                count += 1
    return count

for i in range(n):
    for j in range(n):
        if graph[i][j] == '1' and not visited[i][j]:
            count = bfs(i, j)
            counts.append(count)

counts.sort() # 정렬 조건이 있었음을 체크 !!!
print(len(counts))
print(*counts, sep='\n')

# 정리
# 방문 체크에 대해 중복으로 처리하지는 않았는지 점검할 것.
# 메모리 누수에 대해서 민감하게 반응할 것!