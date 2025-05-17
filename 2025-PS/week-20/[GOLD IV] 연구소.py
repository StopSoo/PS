# https://www.acmicpc.net/problem/14502

# 내 답안
# 걸린 시간: 1484ms
# 알고리즘/자료구조: 그래프(BFS), 브루트포스 
# 다 구현해놓고 헤맨 부분: virus 함수에 배열 전달할 때 원본 배열 전달한 점(!)
import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

N, M = map(int, input().strip().split())
miro = list(list(map(int, input().strip().split())) for _ in range(N))
virus_pos = [(y, x) for y in range(N) for x in range(M) if miro[y][x] == 2]
ground_pos = [(y, x) for y in range(N) for x in range(M) if miro[y][x] == 0]

def virus(miro):
  deq = deque(virus_pos)
  dy = [-1, 1, 0, 0]
  dx = [0, 0, -1, 1]

  while deq:
    y, x = deq.popleft()
    for i in range(4): 
      ny, nx = y + dy[i], x + dx[i]
      if 0 <= ny < N and 0 <= nx < M and miro[ny][nx] == 0:
        miro[ny][nx] = 2
        deq.append((ny, nx))
  # 안전영역의 크기 출력
  return sum([1 for i in range(N) for j in range(M) if miro[i][j] == 0])

max_area = 0
for comb in combinations(ground_pos, 3):
  temp_miro = [row[:] for row in miro[:]] # 현재 상태 복사
  
  for y, x in comb: # 벽 세우기
    temp_miro[y][x] = 1
  
  answer = virus(temp_miro)
  max_area = max(max_area, answer)

print(max_area)