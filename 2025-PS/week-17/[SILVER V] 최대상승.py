# https://www.acmicpc.net/problem/25644

# 내 답안
# 걸린 시간: 276ms
# 푸는 데 1시간이나 걸림
import sys
input = sys.stdin.readline

N = int(input())
numbers = [0] + list(map(int, input().strip().split())) # 1 기반 인덱스
dp = [[float('inf'), float('inf')] for _ in range(N+1)] # 산 시점, 판 시점 (1 기반 인덱스)
dp[1] = [numbers[1], numbers[1]] # 지금 사서 지금 파는 것이 가장 이득
for n in range(2, N+1): # dp[n]
  dp[n][1] = numbers[n]
  if dp[n-1][0] > numbers[n]: dp[n][0] = numbers[n]
  else: dp[n][0] = dp[n-1][0]
print(max(dp[i][1] - dp[i][0] for i in range(1, N+1)))

# 2차원 배열을 이용하지 않는 더 간단한 방법
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split(' ')))

minimum = arr[0]
ans = 0
for i in range(1, N):
  minimum = min(minimum, arr[i])
  ans = max(ans, arr[i]-minimum)

print(ans)