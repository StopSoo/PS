# https://www.acmicpc.net/problem/10799

# 내 답안
# 걸린 시간: 84ms
# 나는 덱을 썼지만 그냥 리스트 써도 OK!
import sys 
input = sys.stdin.readline
from collections import deque

deq = deque()
piece = input()
answer = 0 # 잘려진 조각의 개수
for i, p in enumerate(piece):
  if p == '(': deq.append(p)
  elif p == ')':
    deq.pop()
    if piece[i-1] == '(': answer += len(deq) # 레이저
    else: answer += 1 # 끝난 막대

print(answer)