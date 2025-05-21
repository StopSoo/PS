# https://www.acmicpc.net/problem/12865

# 내 답안
# 걸린 시간: 2460ms
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
bp = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (K+1)
for w, v in bp:
  for k in range(K, w - 1, -1):
    dp[k] = max(dp[k], dp[k-w] + v)

print(max(dp))