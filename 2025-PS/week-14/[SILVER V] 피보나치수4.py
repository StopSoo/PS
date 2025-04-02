# https://www.acmicpc.net/problem/10826

# 내 답안
# 걸린 시간: 56ms
# dp 배열의 크기를 n+1로 하는 방법보다, 최대 크기로 초기화해놓고 필요한 부분만 값을 넣는 방법이 오류 날 확률이 낮다 (!)
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 10001
dp[1] = 1
for i in range(2, n+1):
  dp[i] = dp[i-1] + dp[i-2]
print(dp[n])