# https://www.acmicpc.net/problem/9625

# 내 답안
# 걸린 시간: 36ms
dp = [[0, 0] for _ in range(46)]
K = int(input())
dp[1] = [0, 1] # A의 개수, B의 개수
dp[2] = [1, 1]
for i in range(3, 46):
  dp[i] = [dp[i-1][1], dp[i-1][0] + dp[i-1][1]]
print(dp[K][0], dp[K][1])