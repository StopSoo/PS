# https://www.acmicpc.net/problem/2688

# 내 답안
# 시간 초과 ~
dp = [0] * 65
dp[1] = 10

T = int(input())
ns = [int(input()) for _ in range(T)]

for n in range(2, max(ns)+1):
  count = 0
  for number in range(10**(n-1), 10**n):
    if str(number) == ''.join(sorted(str(number))): count += 1
  dp[n] = dp[n-1] + count # 갱신
# 출력 
for n in ns: print(dp[n])

# 복습 코드
# 걸린 시간: 32ms
# 중복 조합 공식: C(n + r - 1, r) (!!!)
import math

T = int(input())
ns = [int(input()) for _ in range(T)]

dp = [0] * 65
for n in range(1, max(ns) + 1):
  dp[n] = math.comb(9 + n, n) # 중복 조합 공식 (!)
# 출력 
for n in ns: print(dp[n])