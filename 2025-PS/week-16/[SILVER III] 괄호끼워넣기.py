# https://www.acmicpc.net/problem/11899

# 내 답안
# 걸린 시간: 60ms
from collections import deque

deq = deque()
word = input()
for ch in word:
  if deq and deq[-1] == '(' and ch == ')': deq.pop()
  else: deq.append(ch)
print(len(deq))