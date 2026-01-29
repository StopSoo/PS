# https://www.acmicpc.net/problem/10866
# 261029 풀이
# 알고리즘: 구현
# 시간: 68ms

import sys
input = sys.stdin.readline
from collections import deque

N = int(input().strip())
deq = deque()
for _ in range(N):
    orders = input().strip().split()
    if orders[0] == "push_front": deq.appendleft(orders[1])
    elif orders[0] == "push_back": deq.append(orders[1])
    elif orders[0] == "pop_front": 
        if deq: print(deq.popleft())
        else: print(-1)
    elif orders[0] == "pop_back": 
        if deq: print(deq.pop())
        else: print(-1)
    elif orders[0] == "size": print(len(deq))
    elif orders[0] == "empty": print(1 if not len(deq) else 0)
    elif orders[0] == "front": 
        if deq: print(deq[0])
        else: print(-1)
    elif orders[0] == "back": 
        if deq: print(deq[-1])
        else: print(-1)