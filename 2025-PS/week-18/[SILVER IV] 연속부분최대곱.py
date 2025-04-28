# https://www.acmicpc.net/problem/2670

# 내 답안
# 걸린 시간: 40ms
# 반올림 시 round는 뒤에 0을 출력하지 않음 (!)
import sys
input = sys.stdin.readline

N = int(input())
numbers = list(float(input().strip()) for _ in range(N))
dp = numbers[:]
for i in range(1, N):
  dp[i] = max(dp[i], dp[i]*dp[i-1])

print("%.3f" % max(dp)) # 방법1
# print(f"{max(dp):.3f}") # 방법2