# https://www.acmicpc.net/problem/17404

# 답안
# 걸린 시간: 48ms
import sys
input = sys.stdin.readline

N = int(input())
pay = list(list(map(int, input().split())) for _ in range(N))

INF = float('inf')
result = INF
for start_color in range(3):
  dp = [[INF] * 3 for _ in range(N)]
  # 1번 집의 색깔을 고정시킴
  dp[0][start_color] = pay[0][start_color]
  for j in range(1, N):
    dp[j][0] = pay[j][0] + min(dp[j-1][1], dp[j-1][2])
    dp[j][1] = pay[j][1] + min(dp[j-1][0], dp[j-1][2])
    dp[j][2] = pay[j][2] + min(dp[j-1][0], dp[j-1][1])
  # 마지막 집은 시작 색과 다른 색만 고려
  for end_color in range(3):
    if end_color != start_color:
      result = min(result, dp[N-1][end_color])

print(result)

