# https://www.acmicpc.net/problem/28278

# 내 답안
# 걸린 시간: 832ms
from collections import deque
import sys
input = sys.stdin.readline

stack = deque()
N = int(input().strip())
for _ in range(N):
  order = input().strip().split()
  if order[0] == '1':
    stack.append(int(order[1]))
  elif order[0] == '2':
    if stack: print(stack.pop())
    else: print(-1)
  elif order[0] == '3':
    print(len(stack))
  elif order[0] == '4':
    if stack: print(0)
    else: print(1)
  else:
    if stack: print(stack[-1]) # 맨 위 정수 출력
    else: print(-1)
