# https://www.acmicpc.net/problem/1235

# 내 답안
# 걸린 시간: 44ms
import sys
input = sys.stdin.readline

N = int(input().strip())
numbers = list(input().strip() for _ in range(N))

k = 0
for i in range(1, len(numbers[0])+1):
  s = set()
  for number in numbers:
    if number[::-1][:i] in s: break
    else: s.add(number[::-1][:i])
  else:
    k = i
    break
print(k)