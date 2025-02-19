# https://www.acmicpc.net/problem/1676

# 내 답안
# 걸린 시간: 40ms
from math import factorial

N = int(input())
result = str(factorial(N))[::-1]
count = 0
for r in result:
  if r == '0': count += 1
  else: break
print(count)