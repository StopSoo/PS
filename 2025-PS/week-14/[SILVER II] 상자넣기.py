# https://www.acmicpc.net/problem/1965

# 내 답안
# 걸린 시간: 148ms
# LIS(가장 긴 증가하는 부분 수열) **
import sys
input = sys.stdin.readline

N = int(input().strip())
boxes = [0] + list(map(int, input().strip().split())) # 1 기반 인덱스
dp = [-1] * (N+1) # 1 기반 인덱스
dp[1] = 1 # [크기, 개수]
for n in range(2, N+1): # dp[n]
  best = 0
  for i in range(1, n):
    if boxes[n] > boxes[i]: # 갱신이 가능한 경우만 체크
      best = max(best, dp[i])
  dp[n] = best+1

print(max(dp[1:]))