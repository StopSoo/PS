# https://www.acmicpc.net/problem/15828

# 내 답안
# 걸린 시간: 168ms (100점 !!)
from collections import deque
import sys
input = sys.stdin.readline

N = int(input().strip())
deq = deque()
while True:
  order = int(input().strip())
  if order == -1: break
  elif order == 0: deq.popleft() # O(1)
  else:
    if len(deq) < N: deq.append(order)

if deq: print(*deq)
else: print("empty")