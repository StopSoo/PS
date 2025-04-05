# https://www.acmicpc.net/problem/16194

# 내 답안
# 걸린 시간: 168ms
N = int(input())
prices = [0] + list(map(int, input().split())) # 1 기반 인덱스

dp = prices[:]
for i in range(2, N+1):
  for j in range(1, i):
    dp[i] = min(dp[i], dp[i-j] + prices[j])
print(dp[N])