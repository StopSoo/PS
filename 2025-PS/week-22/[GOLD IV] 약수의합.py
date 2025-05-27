# https://www.acmicpc.net/problem/17425

# 내 답안
# 걸린 시간: 212ms(pypy3)
# 푸는 데 되게 오래 걸림 ... 계속 시간초과 나서!
# 누적합 할 때 기존 값 계산 배열과 누적합 배열을 따로 구분 짓는 게 나은 듯!
import sys
input = sys.stdin.readline

MAX = 10**6
dp = [1] * (MAX + 1)
s = [0] * (MAX + 1) # 누적합을 위한 배열
# 약수의 합 구하기
for i in range(2, MAX + 1):
  j = 1
  while i*j <= MAX:
    dp[i*j] += i
    j += 1
# 누적합
for i in range(1, MAX + 1): s[i] = s[i-1] + dp[i]
# 입력 처리
T = int(input())
result = []
for _ in range(T):
  N = int(input().strip()) 
  result.append(str(s[N]))

sys.stdout.write('\n'.join(result) + '\n')

# 1 => 1 => 합1
# 2 => 1, 2 => 합3 (소)
# 3 => 1, 3 => 합4 (소)
# 4 => 1, 2, 4 => 합7
# 5 => 1, 5 => 합6 (소)
# 6 => 1, 2, 3, 6 => 합12
# 7 => 1, 7 => 합8 (소)
# 8 => 1, 2, 4, 8 => 합15
# 9 => 1, 3, 9 => 합13
# 10 => 1, 2, 5, 10 => 18
# 12 => 1, 2, 3, 4, 6, 12 => 28 
# 18 => 1, 2, 3, 6, 9, 18 => 39