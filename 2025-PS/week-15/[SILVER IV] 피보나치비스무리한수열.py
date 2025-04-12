# https://www.acmicpc.net/problem/14495

# 내 답안
# 걸린 시간: 36ms
dp = [1] * 117
for i in range(4, 117):
  dp[i] = dp[i-1] + dp[i-3]

n = int(input())
print(dp[n])