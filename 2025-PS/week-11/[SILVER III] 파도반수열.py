# https://www.acmicpc.net/problem/9461

# 내 답안
# 걸린 시간: 40ms
# DP -> 규칙 찾기가 관건 !!
P = [0] * 101
P[1] = 1
P[2] = 1
P[3] = 1
for i in range(4, 101):
  P[i] = P[i-3] + P[i-2]

T = int(input())
for _ in range(T):
  N = int(input())
  print(P[N])