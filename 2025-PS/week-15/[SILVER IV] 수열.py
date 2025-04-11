# https://www.acmicpc.net/problem/2491

# 내 답안
# 걸린 시간: 92ms
import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().strip().split()))
dp1, dp2 = [1] * N, [1] * N # 연속해서 커지거나 / 연속해서 작아지거나
for i in range(1, N):
  if numbers[i] >= numbers[i-1]: dp1[i] = dp1[i-1] + 1
  if numbers[i] <= numbers[i-1]: dp2[i] = dp2[i-1] + 1

print(max(max(dp1), max(dp2)))