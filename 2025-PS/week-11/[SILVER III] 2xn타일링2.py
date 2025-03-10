# https://www.acmicpc.net/problem/11727

# 내 답안
# 걸린 시간: 36ms
# dp는 규칙을 찾는 게 중요 !!
n = int(input())
dp = [0] * (n+2)
dp[1] = 1 # 2x1 세로 1개
dp[2] = 3 # 2x1 세로 2개 / 2x1 가로 2개 / 2x2 1개
# dp[3] = 5 # 2x1 세로 3개 / 2x1 가로 2개, 세로 1개 / 2x2 1개, 2x1 세로 1개 / 2x1 세로 1개, 2x2 1개 / 2x1 세로 1개, 가로 2개
if n >= 3:
  for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % 10007
print(dp[n])