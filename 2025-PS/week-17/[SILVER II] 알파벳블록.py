# https://www.acmicpc.net/problem/27497

# 내 답안
# 걸린 시간: 464ms
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
deq = deque()
last = [] # 블록을 추가한 방향 리스트
for _ in range(N):
  orders = input().strip().split()

  if orders[0] == '1':
    deq.append(orders[1])
    last.append('b')
  elif orders[0] == '2':
    deq.appendleft(orders[1])
    last.append('f')
  elif orders[0] == '3':
    if last and last[-1] == 'f': 
      deq.popleft()
      last.pop()
    elif last and last[-1] == 'b': 
      deq.pop()
      last.pop()

print(''.join(deq) if deq else 0)