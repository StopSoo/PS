# https://www.acmicpc.net/problem/9656

# 내 답안
# 걸린 시간: 36ms
N = int(input())
dp = [0] * 1001
dp[1] = 0 # 1은 상근 승, 0은 상근 패 
dp[2] = 1
dp[3] = 0
for i in range(4, 1001):
  dp[i] = 1 if not (dp[i-1] and dp[i-3]) else 0
print("SK" if dp[N] else "CY")