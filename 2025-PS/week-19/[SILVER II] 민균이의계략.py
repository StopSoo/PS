# https://www.acmicpc.net/problem/11568

# 내 답안
# 걸린 시간: 140ms
import sys
input = sys.stdin.readline

N = int(input())
dp = [1] * (N + 1)
numbers = [0] + list(map(int, input().strip().split()))
for n in range(2, N+1):
  best = 0
  for i in range(1, n):
    if numbers[n] > numbers[i]:
      best = max(best, dp[i])
  dp[n] = best + 1

print(max(dp[1:]))