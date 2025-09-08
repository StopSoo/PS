# https://www.acmicpc.net/problem/17070

# 내 첫 번째 답안
# 걸린 시간: 시간 초과
# 알고리즘: 그래프 -> BFS 사용
import sys
input = sys.stdin.readline
from collections import deque

N = int(input().strip())
miro = [list(map(int, input().strip().split())) for _ in range(N)]

ways = [[0] * N for _ in range(N)]
ways[0][0] = 1
ways[0][1] = 1

deq = deque([(0, 1, 1)]) # (y좌표, x좌표, 가/세/대)
while deq:
  y, x, direction = deq.popleft()
  
  if direction == 1: # 가로
    if x + 1 < N and not miro[y][x+1]: # 가로 체크
      deq.append((y, x + 1, 1))
      ways[y][x+1] += 1
    if y + 1 < N and x + 1 < N and not miro[y+1][x+1] and not miro[y][x+1] and not miro[y+1][x]: # 대각선 체크
      deq.append((y + 1, x + 1, 3))
      ways[y+1][x+1] += 1
  elif direction == 2: # 세로
    if y + 1 < N and not miro[y+1][x]: # 세로 체크
      deq.append((y + 1, x, 2))
      ways[y+1][x] += 1
    if y + 1 < N and x + 1 < N and not miro[y+1][x+1] and not miro[y][x+1] and not miro[y+1][x]: # 대각선 체크
      deq.append((y + 1, x + 1, 3))
      ways[y+1][x+1] += 1
  else: # 대각선
    if x + 1 < N and not miro[y][x+1]: # 가로 체크
      deq.append((y, x + 1, 1))
      ways[y][x+1] += 1
    if y + 1 < N and not miro[y+1][x]: # 세로 체크
      deq.append((y + 1, x, 2))
      ways[y+1][x] += 1
    if y + 1 < N and x + 1 < N and not miro[y+1][x+1] and not miro[y][x+1] and not miro[y+1][x]: # 대각선 체크
      deq.append((y + 1, x + 1, 3))
      ways[y+1][x+1] += 1

print(ways[N-1][N-1])

# 내 두 번째 답안
# 걸린 시간: 40ms
# 알고리즘: DP + 그래프 
# 3차원 배열로 구현하는 게 포인트(!)
import sys
input = sys.stdin.readline

N = int(input().strip())
miro = [list(map(int, input().strip().split())) for _ in range(N)]

dp = [[[0] * N for _ in range(N)] for _ in range(3)] # 3차원 배열(방향, y, x)
dp[0][0][1] = 1 # 오른쪽 끝만 표시!

for i in range(N): # 행
  for j in range(N): # 열
    if miro[i][j]: continue
    # 가로로 밀기
    if j - 1 >= 0:
      dp[0][i][j] += dp[0][i][j-1] + dp[2][i][j-1]
    # 세로로 밀기
    if i - 1 >= 0:
      dp[1][i][j] += dp[1][i-1][j] + dp[2][i-1][j]
    # 대각선으로 밀기
    if i - 1 >= 0 and j - 1 >= 0 and not miro[i-1][j] and not miro[i][j-1]:
      dp[2][i][j] += dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]

print(dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1])