# https://www.acmicpc.net/problem/4153

# 내 답안
while True:
  a, b, c = sorted(map(int, input().split()))
  if a == b == c == 0: break
  if a**2 + b**2 == c**2: print("right")
  else: print("wrong")