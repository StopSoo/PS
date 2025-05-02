# https://www.acmicpc.net/problem/2688

# 내 답안
# 알고리즘 유형: DP
# 또 결과값들 사이에서 연관성을 찾으려다가 풀이 실패 ... 
# 중복 조합을 이용한다는 힌트를 보고 combinations_with_replacement를 사용했으나, 브루트포스 방법이라 시간 초과를 피할 수 없음.
from itertools import combinations_with_replacement

T = int(input())
ns = list(int(input()) for _ in range(T))

dp = [0] * 65
dp[1] = 10 # 0~9
for i in range(2, max(ns)+1):
  count = 0
  for cwr in combinations_with_replacement(range(10), i): count += 1
  dp[i] = count
for number in ns:
  print(dp[number])

# 정답 코드
# 걸린 시간: 32ms
# 1. dp[i] = (9+i)C(i)로 구할 수 있다 (!) -> 중복 조합의 경우의 수 계산 공식을 이용한 것 !!
# 우리는 0~9 이렇게 10개의 숫자에서 중복을 허용해 i개의 숫자를 고르고 싶으므로, (10 + i - 1)C(i)인 것임.
# 2. math.comb는 nCk 조합을 계산하는 함수이다.
import math

T = int(input())
ns = [int(input()) for _ in range(T)]

max_n = max(ns)
dp = [0] * (max_n + 1)
for i in range(1, max_n + 1):
  dp[i] = math.comb(9 + i, i)  # 조합 공식 사용

for number in ns: print(dp[number])
