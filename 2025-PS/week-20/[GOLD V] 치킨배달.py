# https://www.acmicpc.net/problem/15686

# 내 답안
# 1시간 반이나 풀다가 결국 포기하고 GPT 행 ;; 
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().strip().split())
miro = list(list(map(int, input().strip().split())) for _ in range(N))
sum_dist = [[0] * N for _ in range(N)] # 모든 집에서 각 치킨집에 도달하는 거리의 합
count = [[0] * N for _ in range(N)] # 이 치킨집을 구독하는 집의 개수

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(N):
  for j in range(N):
    if miro[i][j] == 1:
      visited = [[0] * N for _ in range(N)]
      visited[i][j] = 1 # 방문 체크
      deq = deque()
      deq.append((i, j, 0))
      min_dist = float('inf')

      while deq:
        y, x, cnt = deq.popleft()
        for k in range(4):
          ny, nx = y + dy[k], x + dx[k]
          if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
            if miro[ny][nx] == 0 or miro[ny][nx] == 1: deq.append((ny, nx, cnt + 1))
            elif miro[ny][nx] == 2: 
              # 구독하는 치킨집이 결정되지 않았거나, 구독하는 치킨집과 현재 보는 치킨집의 거리가 같을 때 (둘 다 구독 가능)
              if min_dist == float('inf') or cnt + 1 == min_dist: 
                count[ny][nx] += 1 # 이 치킨집을 구독하는 집의 개수 증가
                min_dist = cnt + 1
              deq.append((ny, nx, cnt + 1))
              sum_dist[ny][nx] += cnt + 1
            visited[ny][nx] = 1 # 방문 체크

answer = 0
count = sorted([(y, x) for y in range(N) for x in range(N) if count[y][x] != 0], key=lambda pos: [count[pos[0]][pos[1]], -sum_dist[pos[0]][pos[1]]], reverse=True)[:M]
for i in range(N):
  for j in range(N):
    if miro[i][j] == 1:
      min_dist = float('inf')
      for k in range(len(count)):
        dist = abs(count[k][0] - i) + abs(count[k][1] - j)
        min_dist = min(min_dist, dist)
      answer += min_dist

print(answer)

# 브루트포스 풀이.
# 걸린 시간: 548ms
import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().strip().split())
miro = [list(map(int, input().strip().split())) for _ in range(N)]

# 집과 치킨집 좌표 수집
houses = []
chickens = []
for i in range(N):
  for j in range(N):
    if miro[i][j] == 1: houses.append((i, j))
    elif miro[i][j] == 2: chickens.append((i, j))

# 치킨집 M개를 고르는 모든 조합을 고려
answer = float('inf')
for chicken_comb in combinations(chickens, M):
  city_dist = 0
  # 각 집에 대해 가장 가까운 치킨집 거리 계산
  for hy, hx in houses:
    min_dist = float('inf')
    for cy, cx in chicken_comb:
      dist = abs(hy - cy) + abs(hx - cx)
      min_dist = min(min_dist, dist)
    city_dist += min_dist
  answer = min(answer, city_dist)

print(answer)

# 백트래킹 풀이
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

# 집과 치킨집 위치 저장
for i in range(N):
  for j in range(N):
    if miro[i][j] == 1: houses.append((i, j))
    elif miro[i][j] == 2: chickens.append((i, j))

answer = float('inf')
selected = []

def get_city_chicken_distance(selected_chickens):
  total = 0
  for hy, hx in houses:
    min_dist = float('inf')
    for cy, cx in selected_chickens:
      dist = abs(hy - cy) + abs(hx - cx)
      min_dist = min(min_dist, dist)
    total += min_dist
  return total

def backtrack(start, selected):
  global answer

  if len(selected) == M: # M개의 치킨집 선택 완료
    city_dist = get_city_chicken_distance(selected)
    answer = min(answer, city_dist)
    return

  for i in range(start, len(chickens)):
    selected.append(chickens[i])
    backtrack(i + 1, selected)
    selected.pop()

backtrack(0, [])
print(answer)