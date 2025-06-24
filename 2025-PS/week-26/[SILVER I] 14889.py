# https://www.acmicpc.net/problem/14889

# 내 답안
# 걸린 시간: 964ms
# 알고리즘: 브루트포스
import sys
input = sys.stdin.readline
from itertools import combinations    

N = int(input())
powers = list(list(map(int, input().split())) for _ in range(N))

def calculate_gap(start, link):
  point_s, point_l = 0, 0
  for i, j in combinations(start, 2):
    point_s += powers[i][j] + powers[j][i]
  for i, j in combinations(link, 2):
    point_l += powers[i][j] + powers[j][i]
  
  return abs(point_s - point_l)

min_gap = float('inf')
# 팀 고르기 (0번 사람을 start 팀에 넣기)
for start in combinations(range(1, N), N // 2 - 1):
  start_team = (0, ) + start
  link_team = [i for i in range(N) if i not in start_team]

  gap = calculate_gap(start_team, link_team)
  if gap == 0:
    print(0)
    sys.exit(0)
  min_gap = min(min_gap, gap)

print(min_gap)

# 백트래킹
# 걸린 시간: 1968ms
import sys
input = sys.stdin.readline

N = int(input())
powers = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
min_gap = float('inf')

def calculate_gap():
  global min_gap
  start, link = [], []

  for i in range(N):
    if visited[i]: start.append(i)
    else: link.append(i)
  
  point_s = point_l = 0
  for i in range(len(start)):
    for j in range(i + 1, len(start)):
      point_s += powers[start[i]][start[j]] + powers[start[j]][start[i]]
      point_l += powers[link[i]][link[j]] + powers[link[j]][link[i]]

  min_gap = min(min_gap, abs(point_s - point_l))

  if min_gap == 0:
    print(0)
    sys.exit(0)

def dfs(depth, idx):
  if depth == N // 2:
    calculate_gap()
    return

  for i in range(idx, N):
    if not visited[i]:
      visited[i] = True
      dfs(depth + 1, i + 1)
      visited[i] = False

dfs(0, 0)
print(min_gap)