# https://www.acmicpc.net/problem/17144

# 내 답안
# 걸린 시간:
import sys
input = sys.stdin.readline

R, C, T = map(int, input().strip().split())
room = list(list(map(int, input().strip().split())) for _ in range(R))
# 공기청정기의 행 위치 구하기
air_cleaner = []
for r in range(R):
  if room[r][0] == -1: 
    air_cleaner.append(r)

def spread():
  temp = [[0]*C for _ in range(R)]
  for r in range(R):
    for c in range(C):
      if room[r][c] > 0:
        spread_amount = room[r][c] // 5
        count = 0
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
          nr, nc = r + dr, c + dc
          if 0 <= nr < R and 0 <= nc < C and room[nr][nc] != -1:
            temp[nr][nc] += spread_amount
            count += 1
        room[r][c] -= spread_amount * count
  for r in range(R):
    for c in range(C):
      room[r][c] += temp[r][c]

def operate():
  top = air_cleaner[0]
  bottom = air_cleaner[1]

  # 위쪽 (반시계 방향)
  for i in range(top-1, 0, -1):
    room[i][0] = room[i-1][0]
  for i in range(C-1):
    room[0][i] = room[0][i+1]
  for i in range(top):
    room[i][C-1] = room[i+1][C-1]
  for i in range(C-1, 1, -1):
    room[top][i] = room[top][i-1]
  room[top][1] = 0

  # 아래쪽 (시계 방향)
  for i in range(bottom+1, R-1):
    room[i][0] = room[i+1][0]
  for i in range(C-1):
    room[R-1][i] = room[R-1][i+1]
  for i in range(R-1, bottom, -1):
    room[i][C-1] = room[i-1][C-1]
  for i in range(C-1, 1, -1):
    room[bottom][i] = room[bottom][i-1]
  room[bottom][1] = 0

for _ in range(T):
  spread()
  operate()

total_dust = sum(sum(cell for cell in row if cell > 0) for row in room)
print(total_dust)