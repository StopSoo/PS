# https://www.acmicpc.net/problem/1699

# 내 첫 번째 답안
# 시간 초과 나는 코드. 그리고 사실 DP랑 거리가 멈.
import math

N = int(input())
dp = [float('inf')] * (N+1)
squares = [] # 제곱수
for i in range(1, N+1):
  if int(math.sqrt(i))**2 == i: # 제곱수라면
    dp[i] = 1
    squares.append(i)
  else:
    for sq in range(len(squares)):
      num = i
      count = 0
      for e in sorted(squares, reverse=True)[sq:]:
        count += num // e
        num %= e
        if num == 0: 
          dp[i] = min(dp[i], count)
          break

print(dp[N])

# 내 두번째 답안
# 걸린 시간: 684ms(pypy3)
# 시간초과를 어떻게 해결할까, DP를 어떻게 적용할까 고민하면서 짜본 코드.
# 이 문제 하나 푸는 데 1시간 넘게 걸린 듯;;
import math

N = int(input())
dp = [0] + [float('inf')] * N
squares = [] # 제곱수
for i in range(1, N+1):
  if int(math.sqrt(i))**2 == i: # 제곱수라면
    dp[i] = 1
    squares.append(i)
  else:
    for sq in sorted(squares, reverse=True):
      dp[i] = min(dp[i], i//sq + dp[i%sq])

print(dp[N])

# 다른 사람의 정답
# 1부터 제곱수를 뺀 것의 dp값에 1을 더한 것이랑 비교 (!)
import sys
import math
input = sys.stdin.readline

n = int(input())
dp = [100000] * (n+1)
for i in range(1, n+1):
  if math.sqrt(i) == int(math.sqrt(i)):
    dp[i] = 1
  else:
    for j in range(1, int(math.sqrt(i))+1):
      dp[i] = min(dp[i], dp[i-j**2]+1)
print(dp[n])