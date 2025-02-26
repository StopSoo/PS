# https://www.acmicpc.net/problem/11048

# 내 답안
# 걸린 시간: 1768ms
# deepcopy에서 막혀서 한참을 해매긴 했는데, 시간 복잡도도 커서 시간을 줄일 수 있는 방법을 생각해야 할 듯
# 리스트 복사 시 copy.deepcopy()를 이용하거나 리스트[:]를 이용하기 (!) 
import copy
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
pos = []
for _ in range(N):
  pos.append(list(map(int, input().strip().split())))
dp = copy.deepcopy(pos) # 깊은 복사가 내가 계속 놓치고 있는 부분이었음 (!)

for x in range(N):
  for y in range(M):
    if (x+1) != N:
      dp[x+1][y] = max(dp[x+1][y], pos[x+1][y] + dp[x][y])
    if (y+1) != M:
      dp[x][y+1] = max(dp[x][y+1], pos[x][y+1] + dp[x][y])
    if (x+1) != N and (y+1) != M:
      dp[x+1][y+1] = max(dp[x+1][y+1], pos[x+1][y+1] + dp[x][y])

print(dp[N-1][M-1])

# 다른 사람의 답안
# 걸린 시간: 404ms
# 풀이 방법: 첫 행, 첫 열만 구해놓고 나머지는 (max 값 + 그 위치의 사탕 개수)로 채우기
import sys

def solve():
  n, m = map(int, sys.stdin.readline().split())
  candy = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

  dp = [[0] * m for _ in range(n)]

  dp[0][0] = candy[0][0]

  for j in range(1, m):
    dp[0][j] = dp[0][j-1] + candy[0][j]

  for i in range(1, n):
    dp[i][0] = dp[i-1][0] + candy[i][0]

  for i in range(1, n):
    for j in range(1, m):
      dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + candy[i][j]

  print(dp[n-1][m-1])

if __name__ == "__main__":
  solve()