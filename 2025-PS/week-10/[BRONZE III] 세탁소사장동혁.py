# https://www.acmicpc.net/problem/2720

# 내 답안
# 걸린 시간: 60ms
T = int(input())
for _ in range(T):
  money = int(input())
  q = money // 25
  money %= 25
  d = money // 10
  money %= 10
  n = money // 5
  money %= 5
  p = money
  print(q, d, n, p)