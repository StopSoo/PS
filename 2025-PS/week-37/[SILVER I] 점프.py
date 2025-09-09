# https://www.acmicpc.net/problem/1890

# 내 답안
# 걸린 시간: 36ms
# 알고리즘: DP
# 또 문제를 대충 읽어서 잘못 풀고 있었음 ... 꼼꼼히 읽으세욧 -> "점프는 딱 한 방향으로만"
N = int(input())
gamepan = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1 # 시작점

for i in range(N):
  for j in range(N):
    jump = gamepan[i][j]
    if jump == 0: 
      continue
    if i + jump < N:
      dp[i + jump][j] += dp[i][j]
    if j + jump < N:
      dp[i][j + jump] += dp[i][j]

print(dp[N-1][N-1])