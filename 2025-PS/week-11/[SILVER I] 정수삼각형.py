# https://www.acmicpc.net/problem/1932

# 내 답안
# 걸린 시간: 124ms
# DP !!
import sys
input = sys.stdin.readline

n = int(input())
numbers = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * i for i in range(1, n+1)]

dp[0][0] = numbers[0][0]
for i in range(1, n):
  for j in range(i+1):
    if j == 0: # 맨 좌측
      dp[i][j] = dp[i-1][j] + numbers[i][j]
    elif j == i: # 맨 우측
      dp[i][j] = dp[i-1][j-1] + numbers[i][j]
    else:
      dp[i][j] = max(dp[i-1][j-1] + numbers[i][j], dp[i-1][j] + numbers[i][j])

print(max(dp[n-1]))