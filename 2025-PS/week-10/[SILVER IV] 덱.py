# https://www.acmicpc.net/problem/10866

# 내 답안
# 걸린 시간: 72ms
# 시간 제한은 0.5초이나, N이 최대 10000이라서 오케이.
import sys
input = sys.stdin.readline
from collections import deque

deq = deque()
N = int(input().strip())
for _ in range(N):
  order = input().strip().split()
  if order[0] == "push_front": deq.appendleft(int(order[1]))
  elif order[0] == "push_back": deq.append(int(order[1]))
  elif order[0] == "pop_front": print(deq.popleft() if deq else -1)
  elif order[0] == "pop_back": print(deq.pop() if deq else -1)
  elif order[0] == "size": print(len(deq))
  elif order[0] == "empty": print(1 if not deq else 0)
  elif order[0] == "front": print(deq[0] if deq else -1)
  elif order[0] == "back": print(deq[-1] if deq else -1)