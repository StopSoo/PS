# https://www.acmicpc.net/problem/13699

# 내 답안
# 걸린 시간: 32ms
dp = [1] * 36
for i in range(1, 36):
  result = 0
  for j in range(i):
    result += dp[j]*dp[i-1-j]
  dp[i] = result

n = int(input())
print(dp[n])