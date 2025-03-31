# https://www.acmicpc.net/problem/11052

# 내 답안
# 걸린 시간: 168ms
# dp[i]: i장의 카드를 구매했을 때의 최대 가격.
# i장 뭉치를 사는 것과 (i-n)장 뭉치와 n장 뭉치를 사는 것의 가격을 비교.
import sys
input = sys.stdin.readline
import math

N = int(input().strip())
prices = [0] + list(map(int, input().strip().split())) # 1기반 인덱스

dp = prices[:]
for i in range(2, N+1):
  for j in range(1, i):
    dp[i] = max(dp[i], dp[i-j] + prices[j])
print(dp[N])