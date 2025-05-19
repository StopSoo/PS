# https://www.acmicpc.net/problem/2225

# 내 답안
# 시간 초과 ~
from itertools import product # 중복 순열 (!)

N, K = map(int, input().split())
MOD = 1000000000
count = 0
for p in product(range(0, N+1), repeat=K):
  if sum(p) == N: count += 1

print(count % MOD)

# 답안
# 걸린 시간: 1208ms
# "부분 문제로 쪼개서 푸는" 전형적인 DP 문제.
# dp[k][n] = 정수 k개를 더해서 합이 n이 되는 경우의 수
# dp[k-1][n]: k-1개의 수로 이미 n을 만들고 0을 더한 경우
# dp[k][n-1]: k개의 수로 n-1을 만들고 1을 더한 경우 (마지막 수가 0보다 큰 수인 경우를 고려한 누적)
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[1] + [0]*(N) for _ in range(K+1)] # 합이 0이 되는 경우의 수는 몇 개의 수더라도 1가지이므로.
dp[1][1] = 1
for k in range(1, K+1):
  for n in range(1, N+1):
    dp[k][n] = (dp[k-1][n] + dp[k][n-1]) % 1000000000
print(dp[K][N])