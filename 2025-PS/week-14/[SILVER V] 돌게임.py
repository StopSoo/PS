# https://www.acmicpc.net/problem/9655

# 내 답안
# 걸린 시간: 44ms
# DP !!
# IndexError -> dp 배열 초기화할 때 너무 큰 값이 아니라면 최대값의 크기로 초기화할 것 (!)
N = int(input())
dp = [0] * 1001 # 0은 상근 패, 1은 상근 승
dp[1] = 1 # 돌이 1개면 무조건 상근 승
dp[2] = 0 # 돌이 2개면 무조건 상근 패
for i in range(3, N+1):
  dp[i] = 1 if not(dp[i-3] and dp[i-1]) else 0

print("SK" if dp[N] else "CY")

# dp[3] = 1 => 0 _ 0
# dp[4] = 0 => 1 _ 1
# dp[5] = 1 => 0 _ 0

# 내 두번째 답안
N = int(input())
dp = [0] * 1001 # 0은 상근 패, 1은 상근 승
dp[1] = 1 # 돌이 1개면 무조건 상근 승
dp[2] = 0 # 돌이 2개면 무조건 상근 패
for i in range(3, N+1):
  if i % 2 == 0: dp[i] = 0
  else: dp[i] = 1

print("SK" if dp[N] else "CY")