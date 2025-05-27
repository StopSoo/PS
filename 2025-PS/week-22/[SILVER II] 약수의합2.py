# https://www.acmicpc.net/problem/17427

# 내 답안
# 걸린 시간: 168ms(pypy3)
import sys
input = sys.stdin.readline

N = int(input())
dp = [0] + [1] * N
s = [0] * (N + 1) # 누적합을 위한 배열
# 약수의 합 구하기
for i in range(2, N + 1):
  j = 1
  while i * j <= N:
    dp[i * j] += i
    j += 1
# 입력 처리
print(sum(dp[:N+1]))