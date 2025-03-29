# https://www.acmicpc.net/problem/16953

# 내 답안
# 걸린 시간: 124ms
# BFS요 !!
# int(str(n1)+'1') = n1*10 + 1 이렇게 할 수도 있음을!! 너무 문자열에 집착하지 말 것.
from collections import deque
import sys
input = sys.stdin.readline

A, B = map(int, input().strip().split())
deq = deque([(A, B, 1)])

answer = 0
while deq:
  n1, n2, count = deq.popleft()
  
  if n1 > n2: continue
  if n1 == n2: 
    answer = count
    break
  deq.append((n1*2, n2, count+1))
  deq.append((int(str(n1) + '1'), n2, count+1))

print(answer if answer != 0 else -1)