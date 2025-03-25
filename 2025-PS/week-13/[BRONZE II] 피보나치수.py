# https://www.acmicpc.net/problem/2747

# 내 답안
# 걸린 시간: 36ms
def fibonacci(n):
  dp = [0] * 46
  dp[1] = 1
  for i in range(2, 46):
    dp[i] = dp[i-1] + dp[i-2]
  return dp[n]

n = int(input())
print(fibonacci(n))