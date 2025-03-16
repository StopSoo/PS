# https://www.acmicpc.net/problem/5086

# 내 답안
# 걸린 시간: 32ms
while True:
  a, b = map(int, input().split())
  if a == 0 and b == 0: break
  if b % a == 0: print("factor")
  elif a % b == 0: print("multiple")
  else: print("neither")
