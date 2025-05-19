# https://www.acmicpc.net/problem/16493

# 내 답안
# 걸린 시간: 48ms
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
books = [list(map(int, input().strip().split())) for _ in range(M)]

dp = [0] * (N + 1)
for day, page in books:
  for i in range(N, day - 1, -1):
    dp[i] = max(dp[i], dp[i - day] + page)

print(max(dp))