# https://www.acmicpc.net/problem/1941

# 내 답안
# 걸린 시간: 1752ms
# 알고리즘: 백트래킹으로 하려다가 BFS로 틀었음.
# 내가 놓친 흐름: 백트래킹이나 조합으로 7명을 뽑고, BFS를 통해 그 7명의 위치가 연결되어있는지를 탐색해야 함(!)
# 개선 포인트 1) count_S를 먼저 수행해서 가지치기하기
# 개선 포인트 2) bfs 수행 시 points 집합을 set화하기
# 개선 포인트 3) count_S 함수에서 s가 4 이상이 될 경우 바로 True 반환하기
import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

students = [list(input()) for _ in range(5)]
positions = [(i, j) for i in range(5) for j in range(5)]

def bfs(y, x, points):
  q = deque([(y, x)])
  visited = [[0] * 5 for _ in range(5)]
  visited[y][x] = 1
  connected_count = 1
  points_set = set(points) # 집합으로 변경해서 O(1)의 시간 복잡도로 변경(!)

  while q:
    ny, nx = q.popleft()
    for dy, dx in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
      new_y, new_x = ny + dy, nx + dx
      if 0 <= new_y < 5 and 0 <= new_x < 5 and not visited[new_y][new_x]: # 방문 체크 꼭 하기 (!)
        if (new_y, new_x) in points_set: 
          connected_count += 1
          visited[new_y][new_x] = 1
          q.append((new_y, new_x))
  
  return connected_count == 7

def count_S(points):
  s = 0
  for y, x in points:
    if students[y][x] == 'S': 
      s += 1
      if s >= 4: 
        return True
  return False

answer = 0 # 경우의 수
for comb in combinations(positions, 7): # 7명 뽑기
  if not count_S(comb): # 뽑힌 조합이 S가 4개 이상 포함되어있지 않다면 pass
    continue
  if bfs(comb[0][0], comb[0][1], comb): # BFS로 7개의 점들이 연결되어 있는지 판단하기
    answer += 1
print(answer)